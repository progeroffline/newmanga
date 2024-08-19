import httpx
from typing import Generator, Literal
from .. import constants, formatters, queries_data
from ..typing.responses import PopularResponse
from ..errors import CatalogueTooManyRequestsError


class Popular:
    """
    A class to handle popular manga queries.

    Parameters
    ----------
    client : httpx.Client
        An instance of the HTTP client used to make requests to the API.
    """

    def __init__(self, client: httpx.Client):
        self.client = client

    def __call__(
        self,
        page: int = 1,
        size: int = 32,
    ) -> PopularResponse:
        """
        Fetch a single page of popular manga.

        Parameters
        ----------
        page : int, optional
            The page number to fetch. Defaults to 1.
        size : int, optional
            The number of items per page. Defaults to 32.

        Returns
        -------
        PopularResponse
            The response containing popular manga information.
        """
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
        """
        Generate popular manga responses page by page.

        Parameters
        ----------
        page : int, optional
            The starting page number. Defaults to 1.
        size : int, optional
            The number of items per page. Defaults to 32.
        scale : Literal["day", "week", "month"], optional
            The time scale for popularity. Defaults to "week".

        Yields
        ------
        PopularResponse
            The response containing popular manga information for each page.

        Raises
        ------
        CatalogueTooManyRequestsError
            If too many requests are made in a row.
        """
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
