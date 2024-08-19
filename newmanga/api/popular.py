import httpx
from typing import Generator, Literal

from .. import constants, formatters, queries_data
from ..typing.responses import PopularResponse
from ..errors import CatalogueTooManyRequestsError


class Popular:
    def __init__(self, client: httpx.Client):
        self.client = client

    def __call__(
        self,
        page: int = 1,
        size: int = 32,
    ) -> PopularResponse:
        try:
            return next(self.next_page(page, size))
        except StopIteration:
            return PopularResponse(mangas=[], total=0, page=page)

    def next_page(
        self,
        page: int = 1,
        size: int = 32,
        scale: Literal["day", "week", "month"] = "week",
    ) -> Generator[PopularResponse, None, None]:
        params = queries_data.popular.copy()
        params["scale"] = scale
        params["page"] = page
        params["size"] = size

        while response := self.client.get(constants.popular, params=params):
            if response.status_code in [502, 429]:
                raise CatalogueTooManyRequestsError(
                    "You making too many requests in a row"
                )

            if response.status_code != 200 or len(response.json()["items"]) == 0:
                break

            yield formatters.json_to_popular_response(
                self.client,
                response.json(),
                params["page"],
            )
            params["page"] += 1
