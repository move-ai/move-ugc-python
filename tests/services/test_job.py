"""Unit tests for using the job service."""
import json

import pytest
from gql.transport.exceptions import TransportQueryError

from tests.services.testcases import ServicesTestCase


class TestJobService(ServicesTestCase):
    """Test job service."""

    service_name = "jobs"

    @pytest.mark.parametrize(
        argnames="expand, job_fixture",
        argvalues=[
            (None, "job_create_response"),
            ([], "job_create_response"),
            (["client"], "job_create_response_with_client"),
            (["take"], "job_create_response_with_take"),
            (["outputs"], "job_create_response_with_outputs"),
        ],
        ids=[
            "no_expand",
            "empty_expand",
            "expand_client",
            "expand_take",
            "expand_outputs",
        ],
    )
    def test_create(  # noqa: WPS211
        self,
        snapshot,
        request,
        faker,
        expand,
        job_fixture,
    ):
        """Test creating a job.

        This should test -> `ugc.jobs.create()`

        Args:
            snapshot: The snapshot fixture.
            request: The request fixture.
            faker: The faker fixture.
            expand: The expand fixture.
            job_fixture: The job fixture.
        """
        request.getfixturevalue(job_fixture)
        job_model = self.client.jobs.create(
            take_id=faker.uuid4(),
            metadata=json.dumps({}),
            expand=expand,
        )
        suffix = "_".join(expand) if expand else str(expand)
        self.assert_execute(
            snapshot=snapshot,
            name=f"create_mutation_expand_{suffix}",
        )
        snapshot.assert_match(
            job_model.model_dump(),
            name=f"create_response_expand_{suffix}",
        )

    @pytest.mark.parametrize(
        argnames="expand, job_fixture",
        argvalues=[
            (None, "job_retrieve_response"),
            ([], "job_retrieve_response"),
            (["client"], "job_retrieve_response_with_client"),
            (["take"], "job_retrieve_response_with_take"),
            (["outputs"], "job_retrieve_response_with_outputs"),
        ],
        ids=[
            "no_expand",
            "empty_expand",
            "expand_client",
            "expand_take",
            "expand_outputs",
        ],
    )
    def test_retrieve(  # noqa: WPS211
        self,
        snapshot,
        request,
        faker,
        expand,
        job_fixture,
    ):
        """Test creating a job.

        This should test -> `ugc.jobs.create()`

        Args:
            snapshot: The snapshot fixture.
            request: The request fixture.
            faker: The faker fixture.
            expand: The expand fixture.
            job_fixture: The job fixture.
        """
        request.getfixturevalue(job_fixture)
        job_model = self.client.jobs.retrieve(
            id=faker.uuid4(),
            expand=expand,
        )
        suffix = "_".join(expand) if expand else str(expand)
        self.assert_execute(
            snapshot=snapshot,
            name=f"retrieve_query_expand_{suffix}",
        )
        snapshot.assert_match(
            job_model.model_dump(),
            name=f"retrieve_response_expand_{suffix}",
        )

    def test_job_not_found(self, snapshot, faker, job_not_found_response):
        """Test job not found.

        This should test -> `ugc.jobs.retrieve(id='invalid-id')'`

        Args:
            snapshot: The snapshot fixture.
            faker: The faker fixture.
            job_not_found_response: job not found response fixture.
        """
        with pytest.raises(TransportQueryError) as excinfo:
            self.client.takes.retrieve(id=faker.uuid4())
        snapshot.assert_match(
            excinfo.value.errors,  # noqa: WPS441
            name="job_not_found_response",
        )
