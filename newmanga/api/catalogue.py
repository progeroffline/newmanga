import httpx
from typing import Generator, Optional

from .. import constants, formatters, queries_data
from ..typing.responses import CatalogueResponse
from ..errors import CatalogueTooManyRequestsError


class Catalogue:
    def __init__(
        self,
        client: httpx.Client,
    ):
        self.client = client

    def __call__(
        self,
        query: Optional[str] = "*",
        page: Optional[int] = 1,
        size: Optional[int] = 32,
    ) -> CatalogueResponse:
        self.query = query
        self.page = page
        self.size = size
        return next(self.next_page(query, page, size))

    def next_page(
        self,
        query: Optional[str] = "*",
        page: Optional[int] = 1,
        size: Optional[int] = 32,
    ) -> Generator[CatalogueResponse, None, None]:
        json_data = queries_data.catalogue.copy()
        json_data["query"] = query
        json_data["pagination"]["page"] = page
        json_data["pagination"]["size"] = size

        while response := self.client.post(constants.catalogue, json=json_data):
            if response.status_code in [502, 429]:
                raise CatalogueTooManyRequestsError(
                    "You making too many requests in a row"
                )

            if (
                response.status_code != 200
                or len(response.json()["result"]["hits"]) == 0
            ):
                break

            yield formatters.json_to_catalogue_reponse(
                self.client, response.json()["result"]
            )
            json_data["pagination"]["page"] += 1
