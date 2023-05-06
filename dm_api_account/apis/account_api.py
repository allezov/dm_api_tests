from requests import Response
from ..models.registration_module import RegistrationModel
from ..models.reset_password import ResetPassword
from ..models.change_password import ChangePassword
from ..models.change_email import ChangeEmail
from restclient.restclient import Restclient
from dm_api_account.models.user_envelope import UserEnvelopeModel
from dm_api_account.models.user_details_envelope import UserDetailsEnvelopeModel


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(self, json: RegistrationModel, **kwargs) -> Response:
        """
        :param json: registration_model
        Register new user
        :return:
        """

        response = self.client.post(
            path=f"/v1/account",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        return response

    def get_v1_account(self, **kwargs) -> Response:
        """
        Get current user
        :return:
        """

        response = self.client.get(
            path=f"/v1/account",
            **kwargs
        )
        UserDetailsEnvelopeModel(**response.json())
        return response

    def put_v1_account_token(self, token: str, **kwargs) -> Response:
        """
        :param token: str
        Activate registered user
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def post_v1_account_password(self, json: ResetPassword, **kwargs) -> Response:
        """
        :param json: reset_password
        Reset registered user password
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/password",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_password(self, json: ChangePassword, **kwargs) -> Response:
        """
        :param json: change_password
        Change registered user password
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/password",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_email(self, json: ChangeEmail, **kwargs) -> Response:
        """
        :param json: change_email
        Change registered user email
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/email",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response
