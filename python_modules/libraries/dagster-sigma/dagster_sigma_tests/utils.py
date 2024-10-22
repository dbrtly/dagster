from typing import Any, Dict, List

from aioresponses import aioresponses


class RequestToMock:
    def __init__(self, value: Dict[str, Any]) -> None:
        self.value = value

    @property
    def headers(self) -> Dict[str, Any]:
        return self.value["headers"]

    @property
    def body(self) -> str:
        return self.value["data"]

    def urlencoded_form_data(self) -> str:
        return self.value["data"]().decode()


def get_requests(responses: aioresponses) -> List[RequestToMock]:
    return [RequestToMock(value[0].kwargs) for value in responses.requests.values()]