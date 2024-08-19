import httpx
from typing import Generator

from .. import constants, formatters, queries_data
from ..typing.responses import UpdatesResponse
from ..errors import CatalogueTooManyRequestsError


class Updates:
    def __init__(self, client: httpx.Client):
        """
        Initializes the Updates class with an HTTP client.

        Parameters
        ----------
        client : httpx.Client
            An instance of the HTTP client used to make requests to the API.
        """
        self.client = client

    def __call__(
        self,
        page: int = 1,
        size: int = 5,
    ) -> UpdatesResponse:
        """
        Fetches and returns the updates for the specified page and size.

        Parameters
        ----------
        page : int, optional
            The page number to fetch, by default 1.
        size : int, optional
            The number of items per page, by default 5.

        Returns
        -------
        UpdatesResponse
            An object containing the updates response data.
        """
        try:
            return next(self.next_page(page, size))
        except StopIteration:
            return UpdatesResponse(mangas=[], total=0, page=page)

    def next_page(
        self,
        page: int = 1,
        size: int = 5,
    ) -> Generator[UpdatesResponse, None, None]:
        """
        Generator to fetch and yield the updates for each page.

        Parameters
        ----------
        page : int, optional
            The starting page number, by default 1.
        size : int, optional
            The number of items per page, by default 5.

        Yields
        ------
        UpdatesResponse
            An object containing the updates response data for each page.

        Raises
        ------
        CatalogueTooManyRequestsError
            If too many requests are made in a short period, causing the API to return a 429 status code.
        """
        params = queries_data.updates.copy()
        params["page"] = page
        params["size"] = size

        while response := self.client.get(constants.updates, params=params):
            if response.status_code in [502, 429]:
                raise CatalogueTooManyRequestsError(
                    "You are making too many requests in a row"
                )

            if response.status_code != 200 or len(response.json()["items"]) == 0:
                break

            yield formatters.json_to_updates_response(
                self.client,
                response.json(),
                params["page"],
            )
            params["page"] += 1
