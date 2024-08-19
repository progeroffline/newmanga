import httpx

from .. import constants, formatters
from ..typing.responses import TagsResponse


class Tags:
    def __init__(self, client: httpx.Client):
        self.client = client

    def __call__(self) -> TagsResponse:
        response = self.client.get(constants.tags)
        return formatters.json_to_tags_response(response.json())
