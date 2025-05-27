# Singlecam Takes and Jobs

A singlecam take is a take that defines a recording session with only a single camera. A single take can be associated with a single video [source](/move-ugc-python/latest/api-reference/schemas/sources/) file and optional additional [source](/move-ugc-python/latest/api-reference/schemas/sources/) files.

## Creating files

Before creating a singlecam take, you must have a video file uploaded to the API. You can upload a video file using the [create file](/move-ugc-python/latest/getting-started/usage/file/#creating-a-file) method. You can use the same method to create any additional files as well if needed.

## Creating a singlecam take

First, create the singlecam take using the file ids that you have created and uploaded to the API.

Follow [this example](/move-ugc-python/latest/getting-started/usage/take/#creating-a-take) to create a singlecam take without any additional sources and [this example](/move-ugc-python/latest/getting-started/usage/take/#create-a-take-with-additional-files-ie-move-file) to create a singlecam take with additional sources.

## Processing a singlecam take

After creating a singlecam take, you can create a singlecam job using the take id. Please follow [this example](/move-ugc-python/latest/getting-started/usage/job/#creating-a-job) to create a singlecam job.

Apart from creating a job in the given example above, you can also provide specific outputs to be generated for the job. The available list of outputs is given [here](https://move-ai.github.io/move-ugc-api/schema/#outputtype).

```python
import json
job = ugc.jobs.create_singlecam(
    take_id="take-2be2463e-ffa3-419b-beb4-ea0f99c79512",
    oututs=["MAIN_BLEND", "MAIN_GLB"],
    metadata=json.dumps({"foo": "bar"}),
)
```

> Note: After the job is processed successfully, and you provided specific outputs only the specified outputs will be generated. If you do not provide any outputs, all default outputs will be generated (render_video, main_fbx, main_usdc, main_usdz, main_blend, motion_data and render_overlay_video).

## Example of a minimal end-to-end single-camera workflow
```python

from __future__ import annotations

import os
import time
from pathlib import Path
from typing import Generator, Optional

import requests
from tqdm import tqdm
from move_ugc import MoveUgc
from move_ugc.schemas.sources import SourceIn, TakeSourceKey

_CHUNK = 8 << 20  # 8MiB

# ─────────────────────────── helper: upload with progress ────────────────────
def upload_local_file(
    ugc: MoveUgc,
    path: Path,
    file_type: str,
) -> "FileType":
    """
    creates a File record and returns the resulting File object.
    """
    file_rec = ugc.files.create(file_type=file_type)
    with open(path, 'rb') as f:
        requests.put(file_rec.presigned_url, data=f.read())

    return file_rec


# ─────────────────────────── helper: poll job ────────────────────────────────
def wait_for_job(ugc: MoveUgc, job_id: str, every: int = 15) -> "JobType":
    """Poll *job_id* until it reaches a terminal state and return the final Job."""
    terminal = {"FINISHED", "FAILED", "CANCELLED"}
    while True:
        job = ugc.jobs.retrieve(id=job_id)
        state = job.state
        print("Job state:", state)
        if state in terminal:
            return job
        time.sleep(every)

# ─────────────────────────── helper: wait for outputs ───────────────────────
def wait_for_outputs(
    ugc: MoveUgc,
    job_id: str,
    every: int = 10,
    timeout: int = 600,
) -> "JobType":
    """
    Re‑poll the job (expand=["outputs"]) until outputs expose a
    presigned URL, or until *timeout* seconds have elapsed.
    """
    t0 = time.time()
    while True:
        job = ugc.jobs.retrieve(id=job_id, expand=["outputs"])   #  [oai_citation:0‡Move AI](https://move-ai.github.io/move-ugc-python/3.0.1/api-reference/services/job/)
        ready = all(
            asset.file and asset.file.presigned_url              #  [oai_citation:1‡Move AI](https://move-ai.github.io/move-ugc-python/3.1.0/api-reference/schemas/file/)
            for asset in job.outputs
        )
        if ready:
            return job

        if time.time() - t0 > timeout:
            raise TimeoutError(
                f"Outputs not ready after {timeout}s – try a larger timeout?"
            )
        print("Waiting for assets …")        # keeps the user informed
        time.sleep(every)


# ─────────────────────────── helper: download outputs ────────────────────────
def download_outputs(job: "JobType", out_root: Path):
    """
    Download each asset in *job.outputs* into *out_root / <job_id> / …*
    """
    out_dir = out_root / job.id
    out_dir.mkdir(parents=True, exist_ok=True)

    for asset in job.outputs:
        url = asset.file.presigned_url
        fname = f" output{asset.file.type.lower()}"
        dest = out_dir / fname

        print(f"↓ {fname}")
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            total = int(r.headers.get("content-length", 0))
            with tqdm(total=total, unit="B", unit_scale=True) as bar, \
                 dest.open("wb") as fh:
                for chunk in r.iter_content(chunk_size=_CHUNK):
                    fh.write(chunk)
                    bar.update(len(chunk))

        print("Saved ->", dest)


# ─────────────────────────── main workflow ───────────────────────────────────
def main(
    video_path: Path,
    move_path: Optional[Path],
    device_label: str,
    outputs_dir: Path,
):
    api_key = os.getenv("MOVE_API_KEY")
    ugc = MoveUgc(api_key=api_key)

    # 1. Upload required video
    video_file = upload_local_file(ugc, video_path, "mp4")

    # 2. Optionally upload .move metadata
    move_file = (
        upload_local_file(ugc, move_path, "move") if move_path else None
    )

    # 3. Create take
    sources = [
        SourceIn(device_label=device_label,
                 file_id=video_file.id, format=TakeSourceKey.mp4)
    ]
    if move_file:
        sources.append(
            SourceIn(device_label=device_label,
                     file_id=move_file.id, format=TakeSourceKey.move)
        )

    take = ugc.takes.create_singlecam(sources=sources)
    print("Created take:", take.id)

    # 4. Kick off job (full default outputs)
    job = ugc.jobs.create_singlecam(take_id=take.id, outputs=['MAIN_BLEND', 'MAIN_FBX'])
    print("Created job:", job.id)

    # 5. Wait for the solver to finish
    job = wait_for_job(ugc, job.id)
    if job.state != "FINISHED":
        raise RuntimeError(f"Job ended in state {job.state}")

    print("🎉 FINISHED – waiting for assets to be uploaded")
    job = wait_for_outputs(ugc, job.id)  # ← NEW

    print('Downloading outputs to', outputs_dir)
    download_outputs(job, outputs_dir)


# ─────────────────────────── CLI wrapper ─────────────────────────────────────
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Move‑UGC single‑camera example",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--video", required=True, type=Path,
                        help="Path to the .mp4 video file")
    parser.add_argument("--move", type=Path,
                        help="Optional path to .move metadata file")
    parser.add_argument("--device-label", default="iphone",
                        help="Slug identifying the camera (lowercase & hyphens)")
    parser.add_argument("--outputs-dir", default=Path("outputs"), type=Path,
                        help="Directory where outputs should be downloaded")

    args = parser.parse_args()

    main(
        video_path=args.video.expanduser().resolve(),
        move_path=args.move.expanduser().resolve() if args.move else None,
        device_label=args.device_label,
        outputs_dir=args.outputs_dir.expanduser().resolve(),
    )
```