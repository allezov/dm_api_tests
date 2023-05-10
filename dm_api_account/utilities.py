import requests
from pydantic import BaseModel


def validate_request_json(json: dict | BaseModel):
    if isinstance(json, dict):
        return json
    return json.dict(by_alias=True, exclude_none=True)


def validate_status_code(response: requests.Response, status_code: int):
    assert response.status_code == status_code, \
        f"Cтатус код ответа должен быть = {status_code}, но он = {response.status_code}"
