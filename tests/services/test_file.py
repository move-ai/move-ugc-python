"""Unit tests for using the files service."""

import pytest
from gql.transport.exceptions import TransportQueryError

from tests.constants import CLIENT_LITERAL
from tests.services.testcases import ServicesTestCase


class TestFileService(ServicesTestCase):
    """Test file service."""

    service_name = "files"

    @pytest.mark.parametrize(
        argnames="expand, file_fixture",
        argvalues=[
            (None, "file_retrieve_response"),
            ([], "file_retrieve_response"),
            ([], "file_retrieve_response_no_thumbnail"),
            ([CLIENT_LITERAL], "file_retrieve_response_with_client"),
        ],
        ids=["no_expand", "empty_expand", "empty_expand_no_thumbnail", "expand_client"],
    )
    def test_retrieve(  # noqa: WPS211
        self,
        expand,
        snapshot,
        snapshot_json,
        faker,
        request,
        file_fixture,
    ):
        """Test retrieving a file from Move UGC API.

        This should test -> `ugc.files.retrieve(id='files-<uuid>, expand=[<fixture>])'`

        Args:
            expand: The expand fixture.
            snapshot: The snapshot fixture.
            snapshot_json: The snapshot JSON fixture.
            faker: The faker fixture.
            request: The request fixture.
            file_fixture: The file fixture.
        """
        request.getfixturevalue(file_fixture)
        file_model = self.client.files.retrieve(id=faker.uuid4(), expand=expand)
        suffix = "_".join(expand) if expand else str(expand)
        self.assert_execute(
            snapshot,
            name=f"retrieve_query_expand_{suffix}",
        )
        assert file_model.model_dump() == snapshot_json(
            name=f"file_retrieve_response_expand_{suffix}",
        )

    def test_file_not_found(self, snapshot, faker, file_not_found_response):
        """Test file not found.

        This should test -> `ugc.files.retrieve(id='invalid-id')'`

        Args:
            snapshot: The snapshot fixture.
            faker: The faker fixture.
            file_not_found_response: The file not found response fixture.
        """
        with pytest.raises(TransportQueryError) as excinfo:
            self.client.files.retrieve(id=faker.uuid4(), expand=[CLIENT_LITERAL])
        assert excinfo.value.errors == snapshot(  # noqa: WPS441
            name="file_not_found_response",
        )

    @pytest.mark.parametrize(
        argnames="expand, file_fixture",
        argvalues=[
            (None, "file_create_response"),
            ([], "file_create_response"),
            ([CLIENT_LITERAL], "file_create_response_with_client"),
        ],
        ids=["no_expand", "empty_expand", "expand_client"],
    )
    def test_create(  # noqa: WPS211
        self,
        expand,
        snapshot,
        snapshot_json,
        faker,
        request,
        file_fixture,
    ):
        """Test creating a file from Move UGC API.

        This should test -> `ugc.files.create(id='files-<uuid>, expand=[<fixture>])'`

        Args:
            expand: The expand fixture.
            snapshot: The snapshot fixture.
            snapshot_json: The snapshot JSON fixture.
            faker: The faker fixture.
            request: The request fixture.
            file_fixture: The file fixture.
        """
        request.getfixturevalue(file_fixture)
        file_model = self.client.files.create(
            file_type=faker.file_extension(),
            metadata=request.getfixturevalue("metadata_for_update"),
            expand=expand,
        )
        suffix = "_".join(expand) if expand else str(expand)
        self.assert_execute(
            snapshot,
            name=f"create_mutation_expand_{suffix}",
        )
        assert file_model.model_dump() == snapshot_json(
            name=f"create_mutation_response_expand_{suffix}",
        )

    @pytest.mark.parametrize(
        argnames="expand, file_fixture",
        argvalues=[
            (None, "file_update_response"),
            ([], "file_update_response"),
            ([CLIENT_LITERAL], "file_update_response_with_client"),
        ],
        ids=["no_expand", "empty_expand", "expand_client"],
    )
    def test_update(  # noqa: WPS211
        self,
        expand,
        snapshot,
        snapshot_json,
        faker,
        request,
        file_fixture,
    ):
        """Test creating a file from Move UGC API.

        This should test -> `ugc.files.create(id='files-<uuid>, expand=[<fixture>])'`

        Args:
            expand: The expand fixture.
            snapshot: The snapshot fixture.
            snapshot_json: The snapshot JSON fixture.
            faker: The faker fixture.
            request: The request fixture.
            file_fixture: The file fixture.
        """
        request.getfixturevalue(file_fixture)
        file_model = self.client.files.update(
            id=faker.uuid4(),
            metadata=request.getfixturevalue("metadata_for_update"),
            name=faker.name(),
            expand=expand,
        )
        suffix = "_".join(expand) if expand else str(expand)
        self.assert_execute(
            snapshot,
            name=f"update_mutation_expand_{suffix}",
        )
        assert file_model.model_dump() == snapshot_json(
            name=f"update_mutation_response_expand_{suffix}",
        )

    def test_generate_share_code(
        self,
        share_code_response,
        faker,
        snapshot,
        snapshot_json,
    ):
        """Test generating a share code from Move UGC API.

        Args:
            share_code_response: The share code response fixture.
            faker: The faker fixture.
            snapshot: The snapshot fixture.
            snapshot_json: The snapshot JSON fixture.
        """
        share_code = self.client.files.generate_share_code(file_id=faker.uuid4())
        self.assert_execute(snapshot, name="generate_share_code_mutation")

        assert share_code.model_dump() == snapshot_json(
            name="generate_share_code_mutation_response",
        )
