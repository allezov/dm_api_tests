import json

import allure
from dm_api_account.models import LoginCredentials


class Login:
    def __init__(self, facade):
        from services.dm_api_account import Facade
        self.facade: Facade = facade

    def set_headers(self, headers):
        """Set the headers in class helper - Login"""
        self.facade.login_api.client.session.headers.update(headers)

    def login_user(self, login: str, password: str, remember_me: bool = True):
        with allure.step('login_user'):
            response = self.facade.login_api.v1_account_login_post(
                _return_http_data_only=False,
                login_credentials=LoginCredentials(
                    login=login,
                    password=password,
                    remember_me=remember_me,
                )
            )
        return response

    def get_auth_token(self, login: str, password: str, remember_me: bool = True):
        with allure.step('get_auth_token'):
            result = self.login_user(login=login, password=password, remember_me=remember_me)
            print('result is ')
            print(type(result))
            return {'X-Dm-Auth-Token': result.headers['X-Dm-Auth-Token']}

    def logout_user(self, **kwargs):
        with allure.step('logout_user'):
            return self.facade.login_api.v1_account_login_delete(**kwargs)

    def logout_user_from_all_devices(self, **kwargs):
        with allure.step('logout_user_all'):
            return self.facade.login_api.v1_account_login_all_delete(**kwargs)
