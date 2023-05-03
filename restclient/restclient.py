import requests.exceptions
from requests import session, Response
import structlog
import uuid
import curlify


class Restclient:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        if headers:
            self.session.headers.update(headers)
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='api')

    def post(self, path: str, **kwargs) -> Response:
        return self._send_requests('POST', path, **kwargs)

    def get(self, path: str, **kwargs) -> Response:
        return self._send_requests('GET', path, **kwargs)

    def put(self, path: str, **kwargs) -> Response:
        return self._send_requests('PUT', path, **kwargs)

    def delete(self, path: str, **kwargs) -> Response:
        return self._send_requests('DELETE', path, **kwargs)

    def _send_requests(self, method, path, **kwargs):
        full_url = self.host + path
        log = self.log.bind(evet_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            method=method,
            full_url=full_url,
            params=kwargs.get('params'),
            headers=kwargs.get('headers'),
            json=kwargs.get('json'),
            data=kwargs.get('data')
        )

        rest_response = self.session.request(
            method=method,
            url=full_url,
            **kwargs
        )

        curl = curlify.to_curl(rest_response.request)
        print(curl)

        log.msg(
            event='response',
            status_code=rest_response.status_code,
            headers=rest_response.headers,
            json=self._get_json(rest_response),
            text=rest_response.text,
            content=rest_response.content,
            curl=curl
        )
        return rest_response

    @staticmethod
    def _get_json(rest_response):
        try:
            return rest_response.json()
        except requests.exceptions.JSONDecodeError:
            return
