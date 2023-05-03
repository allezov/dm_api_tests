from requests import Response
from ..models.login_credentials import login_credentials
from restclient.restclient import Restclient


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(self, json: login_credentials, **kwargs) -> Response:
        """
        :param json: login_credentials
        Authenticate via credentials
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/login",
            json=json,
            **kwargs
        )
        return response

    def del_v1_account_all(self) -> Response:  # delete **kwargs
        """
        Logout from every device
        :return:
        """

        response = self.client.delete(
            path=f"/v1/account/login/all"
        )
        return response

    def del_v1_account_login(self) -> Response:  # delete **kwargs
        """
        Logout as current user
        :return:
        """

        response = self.client.delete(
            path=f"/v1/account/login"
        )
        return response
