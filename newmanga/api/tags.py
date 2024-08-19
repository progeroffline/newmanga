import httpx

from .. import constants, formatters
from ..typing.responses import TagsResponse


class Tags:
    def __init__(self, client: httpx.Client):
        """
        Initializes the Tags class with an HTTP client.

        Parameters
        ----------
        client : httpx.Client
            An instance of the HTTP client used to make requests to the API.
        """
        self.client = client

    def __call__(self) -> TagsResponse:
        """
        Fetches and returns the list of tags.

        Returns
        -------
        TagsResponse
            An object containing the tags response data.
        """
        response = self.client.get(constants.tags)
        return formatters.json_to_tags_response(response.json())
