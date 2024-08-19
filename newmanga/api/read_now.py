import httpx

from .. import constants, formatters
from ..typing.responses import ReadNowResponse


class ReadNow:
    """
    A class to interact with the 'Read Now' feature of the API.

    Parameters
    ----------
    client : httpx.Client
        An instance of the HTTP client used to make requests to the API.
    """

    def __init__(self, client: httpx.Client):
        """
        Initializes the ReadNow class with an HTTP client.

        Parameters
        ----------
        client : httpx.Client
            An instance of the HTTP client used to make requests to the API.
        """
        self.client = client

    def __call__(self) -> ReadNowResponse:
        """
        Fetches and returns the 'Read Now' data.

        Returns
        -------
        ReadNowResponse
            An object containing the data for the 'Read Now' feature.
        """
        response = self.client.get(constants.read_now)
        return formatters.json_to_read_now_response(self.client, response.json())
