"""Unit tests for using the job service."""

import pytest
from gql.transport.exceptions import TransportQueryError
from graphql.execution.execute import ExecutionResult
from pydantic import ValidationError

from tests.constants import LIST_JOBS_QUERY
from tests.services.testcases import ServicesTestCase


class TestJobService(ServicesTestCase):  # noqa: WPS214
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
            metadata=request.getfixturevalue("metadata_for_update"),
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
            (None, "job_create_multicam_response"),
            ([], "job_create_multicam_response"),
            (["client"], "job_create_multicam_with_client"),
            (["take"], "job_create_multicam_with_take"),
            (["outputs"], "job_create_multicam_with_outputs"),
        ],
        ids=[
            "no_expand",
            "empty_expand",
            "expand_client",
            "expand_take",
            "expand_outputs",
        ],
    )
    def test_create_multicam(  # noqa: WPS211
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
        job_model = self.client.jobs.create_multicam(
            take_id=faker.uuid4(),
            metadata=request.getfixturevalue("metadata_for_update"),
            number_of_actors=faker.pyint(),
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

    @pytest.mark.parametrize(
        argnames="take_id",
        argvalues=["take-123-123-123-123", None],
        ids=["with_take_id", "without_take_id"],
    )
    def test_list(self, take_id, snapshot, jobs_list_response):
        """Test listing jobs.

        This should test -> `ugc.jobs.list()`

        Args:
            take_id: The take id fixture.
            snapshot: The snapshot fixture.
            jobs_list_response: job list response fixture.
        """
        job_list = self.client.jobs.list(take_id=take_id)
        self.assert_execute(snapshot, name="job_list_request")
        snapshot.assert_match(
            job_list.model_dump(),
            name="list_response",
        )

    def test_list_job_invalid(self, request, job_not_found_json):
        """Test job errors.

        This should test -> `ugc.jobs.list()`

        Args:
            request: The request fixture.
            job_not_found_json: job not found json fixture.
        """
        mock_transport = request.getfixturevalue("mock_transport")
        fake_list_job_response = request.getfixturevalue("fake_list_job_response")
        introspection_result = request.getfixturevalue("introspection_result")

        fake_list_job_response[LIST_JOBS_QUERY]["items"] = [
            {"id": "dummy-123-123-123-123"},
        ]

        job_response = ExecutionResult(data=fake_list_job_response)
        mock_transport.side_effect = [introspection_result, job_response]

        with pytest.raises(ValidationError) as excinfo:
            self.client.jobs.list()

    def test_list_job_empty(self, request, job_not_found_json):
        """Test job when it has an empty response.

        This should test -> `ugc.jobs.list()`

        Args:
            request: The request fixture.
            job_not_found_json: job not found json fixture.
        """
        mock_transport = request.getfixturevalue("mock_transport")
        fake_list_job_response = request.getfixturevalue("fake_list_job_response")
        introspection_result = request.getfixturevalue("introspection_result")

        fake_list_job_response[LIST_JOBS_QUERY]["items"] = []

        job_response = ExecutionResult(data=fake_list_job_response)
        mock_transport.side_effect = [introspection_result, job_response]

        assert not self.client.jobs.list().items

    def test_update(  # noqa: WPS211
        self,
        snapshot,
        request,
        faker,
    ):
        """Test updating a job.

        This should test -> `ugc.jobs.update()`

        Args:
            snapshot: The snapshot fixture.
            request: The request fixture.
            faker: The faker fixture.
        """
        request.getfixturevalue("jobs_update_response")
        job_model = self.client.jobs.update(
            id=faker.uuid4(),
            name=faker.name(),
            metadata=request.getfixturevalue("metadata_for_update"),
        )
        self.assert_execute(
            snapshot=snapshot,
            name="update_mutation",
        )
        snapshot.assert_match(
            job_model.model_dump(),
            name="update_response",
        )
