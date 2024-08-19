import httpx

from .. import constants, formatters
from ..typing.responses import ReadNowResponse


class ReadNow:
    def __init__(self, client: httpx.Client):
        self.client = client

    def __call__(self) -> ReadNowResponse:
        response = self.client.get(constants.read_now)
        return formatters.json_to_read_now_response(self.client, response.json())
