import httpx
from typing import Generator

from .. import constants, formatters, queries_data
from ..typing.responses import UpdatesResponse
from ..errors import CatalogueTooManyRequestsError


class Updates:
    def __init__(self, client: httpx.Client):
        self.client = client

    def __call__(
        self,
        page: int = 1,
        size: int = 5,
    ) -> UpdatesResponse:
        try:
            return next(self.next_page(page, size))
        except StopIteration:
            return UpdatesResponse(mangas=[], total=0, page=page)

    def next_page(
        self,
        page: int = 1,
        size: int = 5,
    ) -> Generator[UpdatesResponse, None, None]:
        params = queries_data.updates.copy()
        params["page"] = page
        params["size"] = size

        while response := self.client.get(constants.updates, params=params):
            if response.status_code in [502, 429]:
                raise CatalogueTooManyRequestsError(
                    "You making too many requests in a row"
                )

            if response.status_code != 200 or len(response.json()["items"]) == 0:
                break

            yield formatters.json_to_updates_response(
                self.client,
                response.json(),
                params["page"],
            )
            params["page"] += 1
