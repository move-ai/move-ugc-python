## 4.1.0 (2025-06-11)

### Feat

- IST-2861: Implement syrupy

### Fix

- IST-2760: Tests for python 3.12 and 3.13

## 4.0.0 (2025-06-09)

### BREAKING CHANGE

- IST-2718: Deprecating Python 3.8 support

## 3.3.1 (2025-05-28)

### Fix

- adjusted a comment regarding teh default outputs in the latest added example for the single camera end to end test case

## 3.3.0 (2025-05-28)

### Feat

- IST-2724: Attempt to create changelog

## 3.2.0 (2025-05-27)

### Feat

- added an end to end single camera example to the documentation section
- added an end to end single camera example to the documentation section

## 3.1.2 (2025-03-24)

### Fix

- IST-2647 : Updating dependencies
- IST-2647 : Updating dependencies

## 3.1.1 (2025-03-14)

### Fix

- IST-2686: Update docs

## 3.1.0 (2025-03-10)

### Feat

- IST-2581 - Removing the key literal in mack response
- IST-2581 - Deprecating key in favour of format in queries and adding deprecation message on key IST-2474 - Enabling more tests on release pipeline
- IST-2581 - Deprecating key in favour of format in queries and adding deprecation message on key IST-2474 - Enabling more tests in release pipeline
- IST-2581 - Deprecating key in favour of format in queries and adding deprecation message on key IST-2474 : Enabling more tests in release pipeline

## 3.0.1 (2025-02-24)

### Fix

- IST-2621: Update docs for rigs

## 3.0.0 (2025-02-18)

### BREAKING CHANGE

- IST-2638: Move clip window to job from sources

## 2.0.0 (2025-02-12)

## 1.13.0 (2025-02-12)

### BREAKING CHANGE

- IST-2497 - deprecating jobs create endpoint and IST-2591 - Fixing docstrings

### Feat

- IST-2564 - Rigs list endpoint

## 1.12.0 (2025-02-04)

### Feat

- IST-2556 - Allowing rig argument on jobs

## 1.11.0 (2025-01-08)

### Feat

- No Ticket: Pin poetry version
- IST-2524: Allow expansion of volume outputs

## 1.10.0 (2024-12-13)

### Fix

- IST-2429 - Remove development banner
- IST-2429 - Add quickstart docs for both single and multicam

## 1.9.0 (2024-12-11)

### Feat

- IST-2461 - Add ability to ask for specific outputs

## 1.8.0 (2024-12-05)

### Feat

- IST-2297: Adding options in single cam jobs
- IST-2297: Adding options in single cam jobs

## 1.7.0 (2024-11-28)

### Feat

- IST-2361 Updating pytest snapshot
- IST-2361: no-warn-unused-ignores
- IST-2361: Resolve mypy issues
- IST-2361 Adding mypy ignores
- IST-2361 Implementing list camera settings

## 1.6.2 (2024-10-28)

### Fix

- use pydantic version compatible with other ml packages
- use pydantic version compatible with other ml packages

## 1.6.1 (2024-10-24)

### Fix

- IST-2247 - Move camera_settings queries to its own section

## 1.6.0 (2024-10-18)

### Feat

- IST-2249 - This should target main branch hence remove ref
- IST-2249 - Trigger integration tests from move-services-testing

## 1.5.0 (2024-10-18)

### Feat

- IST-1498: listVolumes query

## 1.4.1 (2024-10-04)

### Fix

- IST-1989: This should be None

## 1.4.0 (2024-10-04)

### Feat

- IST-1989: Allow updating the name of the take

## 1.3.0 (2024-10-04)

### Feat

- IST-1990 - IST-1988 - Update name in jobs & files

## 1.2.4 (2024-10-02)

### Fix

- IST-1196: `after` is actually a json string

## 1.2.3 (2024-10-02)

### Fix

- Bump mkdocstrings to 0.26.1

## 1.2.2 (2024-10-02)

### Fix

- Hardcode fake datetimes for sharecode response
- Use freeze time for faker because faker doesn't retain date values in windows
- Bump faker to 30.1.0 manually & update snapshots
- No ticket - Bump mkdocs and mkdocs-material manually
- bump idna from 3.6 to 3.7
- bump zipp from 3.17.0 to 3.19.1
- bump certifi from 2023.11.17 to 2024.7.4
- bump urllib3 from 2.1.0 to 2.2.2
- bump requests from 2.31.0 to 2.32.2
- bump jinja2 from 3.1.3 to 3.1.4
- bump pydantic-settings from 2.1.0 to 2.2.1

## 1.2.1 (2024-10-02)

### Fix

- IST-2058 - Remove integration tests dependency

## 1.2.0 (2024-10-02)

### Feat

- IST-2058 - Update docs and uncomment pypi publish action

## 1.2.0b2 (2024-10-01)

### Feat

- IST-2058 - Add create_singlecam and raise a deprecation warning for .create
- IST-2058 - Add multicam job mutation

## 1.2.0b1 (2024-09-30)

### Feat

- IST-2058 - Add multicam take queries

## 1.2.0b0 (2024-09-27)

### Feat

- IST-2058 - Add integration tests
- IST-2058 - Bump prerelease version and disable release workflow
- IST-2058 - Add getVolume query
- IST-2058 - We can't use StrEnum for python < 3.11
- IST-2058 - Add createVolumeWithHuman mutation

## 1.1.1 (2024-09-24)

### Fix

- IST-2105: Handle thumbnail URL being empty

## 1.1.0 (2024-09-18)

### Feat

- IST-2105: Add thumbnail Url attribute

## 1.0.0 (2024-08-21)

### BREAKING CHANGE

- IST-2143: singlecam API functionality

## 0.9.2 (2024-07-16)

### Fix

- bump setuptools from 69.0.3 to 70.0.0

## 0.9.1 (2024-02-21)

### Fix

- IST-1096 update node version in actions

## 0.9.0 (2024-01-26)

### Feat

- SDT-775 - Add upsertWebhookEndpoint mutation
- SDT-775 - Add ability to share file

### Fix

- SDT-775 - update the link for event catalogue
- SDT-775 - Update docs for upsert webhook

## 0.8.4 (2024-01-26)

### Fix

- SDT-775 - Update docs for updateJob
- SDT-775 - Add updateJob mutation
- SDT-775 - Update docs for authentication & jobs for listing
- SDT-775 - Add tests for error cases
- SDT-775 - Add ability to filter by take_id
- SDT-775 - Add listJobs query

## 0.8.3 (2024-01-25)

### Fix

- SDT-775 - Update docs for listTakes
- SDT-775 - Add listTakes query

## 0.8.2 (2024-01-25)

### Fix

- SDT-775 - update docs for metadata
- SDT-775 - Add updateTake mutation

## 0.8.1 (2024-01-24)

## 0.8.0 (2024-01-24)

### Feat

- SDT-775 - Add retrieve and update client requests

### Fix

- SDT-775 - Updates doc for client and files object + hyper link schemas
- SDT-775 - Add updateFile mutation
- SDT-775 - Add metadata parameter fix to create file mutation
- SDT-775 - Bump pydantic to latest

## 0.7.12 (2023-08-31)

### Fix

- bump faker from 18.13.0 to 19.2.0

## 0.7.11 (2023-08-31)

### Fix

- bump pydantic from 2.0.2 to 2.1.1

## 0.7.10 (2023-08-30)

### Fix

- bump mkdocs-material from 9.1.18 to 9.1.21

## 0.7.9 (2023-08-14)

### Fix

- bump pydantic-settings from 2.0.0 to 2.0.2

## 0.7.8 (2023-08-09)

### Fix

- bump mkdocs from 1.4.3 to 1.5.1

## 0.7.7 (2023-07-26)

### Fix

- Ignore WPS125 in .flake8 [SDT-402]

## 0.7.6 (2023-07-14)

### Fix

- update documentation for package name

## 0.7.5 (2023-07-14)

### Fix

- fix contribution link
- use the correct documentation link

## 0.7.4 (2023-07-13)

### Fix

- change graphql endpoint to target domain name instead

## 0.7.3 (2023-07-13)

### Fix

- use the correct package name and correct ci badge

## 0.7.2 (2023-07-13)

### Fix

- use correct permissions [SDT-418]

## 0.7.1 (2023-07-13)

### Fix

- snapshot update
- add documentation and publish step [SDT-418]

## 0.7.0 (2023-07-12)

### Feat

- add retrieve method for jobs [SDT-382]

## 0.6.2 (2023-07-12)

### Fix

- use correct planned usage in take
- update documentation for jobs service and examples for take

## 0.6.1 (2023-07-11)

### Fix

- bump faker from 17.6.0 to 18.13.0

## 0.6.0 (2023-07-11)

### Feat

- add job service [SDT-381]

### Fix

- change example uuids to be unique

## 0.5.3 (2023-07-10)

### Fix

- bump pytest-randomly from 3.12.0 to 3.13.0

## 0.5.2 (2023-07-10)

### Fix

- bump pydantic from 2.0 to 2.0.2

## 0.5.1 (2023-07-10)

### Fix

- add commit message so that existing/future dependebot PRs don't have package version issues

## 0.5.0 (2023-07-10)

### Feat

- add retrieve take method in take service

### Fix

- fix id param in retrieve calls

## 0.4.0 (2023-07-07)

### Feat

- add take service and docs [SDT-379]

### Fix

- add not support doc for additional files
- add move file key type
- add crosslink to file & use different id for additional file

## 0.3.1 (2023-07-06)

### Fix

- add restriction in tags creation

## 0.3.0 (2023-07-06)

### Feat

- change version provider in commitizen and add pre-commit correctly
- introduce commitizen

## 0.2.5 (2023-07-05)

## 0.2.4 (2023-07-05)

## 0.2.3 (2023-07-05)

## 0.2.2 (2023-07-05)

## 0.2.1 (2023-07-05)

## 0.2.0 (2023-07-05)

## 0.1.0 (2023-07-03)
