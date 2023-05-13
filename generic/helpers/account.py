from dm_api_account.models import Registration


class Account:
    def __init__(self, facade):
        self.facade = facade

    def set_headers(self, headers):
        """Set the headers in class helper - Account"""
        self.facade.account_api.client.session.headers.update(headers)

    def register_new_user(self, login: str, email: str, password: str):
        print('register_new_user started')
        response = self.facade.account_api.post_v1_account(
            json=Registration(
                login=login,
                email=email,
                password=password
            )
        )
        print('register_new_user finished')
        return response

    def activate_registered_user(self, login: str):
        token = self.facade.mailhog.get_token_by_login(login=login)
        response = self.facade.account_api.put_v1_account_token(
            token=token
        )
        return response

    def get_current_user(self, **kwargs):
        return self.facade.account_api.get_v1_account(**kwargs)
