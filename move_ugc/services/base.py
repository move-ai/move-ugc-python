"""Base service class for all services."""
from abc import ABC
from typing import Any, Dict, Generic, Optional, Type, TypeVar, cast

from graphql import DocumentNode
from pydantic import BaseModel

from move_ugc.schemas.metaclient import MetaClient

Schema = TypeVar("Schema", bound=BaseModel)  # Generic template type variable
VariableValues = Optional[Dict[str, Any]]


class BaseService(MetaClient, ABC, Generic[Schema]):
    """Base service class for all services."""

    _schema: Type[BaseModel]

    def serialize(self, query_key: str, response: Dict[str, Dict[str, str]]) -> Schema:
        """Serialize the service object to a Pydantic model.

        Args:
            query_key (str): Key to be used to fetch the object from the response.
            response (Dict[str, Dict[str, str]]): Response from the API.

        Returns:
            Schema: Pydantic model.
        """
        return cast(Schema, self._schema(**response[query_key]))

    def execute(
        self,
        query_key: str,
        gql_query: DocumentNode,
        variable_values: VariableValues = None,
    ) -> Schema:
        """Execute the GraphQL query.

        Args:
            query_key (str): Key to be used to fetch the object from the response.
            gql_query (DocumentNode): GraphQL query.
            variable_values (VariableValues): Variables to be passed to the query. Defaults to None.

        Returns:
            Schema: Pydantic model.
        """
        response = self.ugc_api.execute(gql_query, variable_values=variable_values)
        return self.serialize(query_key=query_key, response=response)
