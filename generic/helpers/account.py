from dm_api_account.models import Registration, ResetPassword, ChangeEmail


class Account:
    def __init__(self, facade):
        self.facade = facade

    def set_headers(self, headers):
        """Set the headers in class helper - Account"""
        self.facade.account_api.client.session.headers.update(headers)

    def register_new_user(self, login: str, email: str, password: str, **kwargs):
        print('register_new_user started')
        # поменять на декоратор
        response = self.facade.account_api.post_v1_account(
            **kwargs,
            json=Registration(
                login=login,
                email=email,
                password=password,
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

    def reset_user_password(self, login: str, email: str):
        response = self.facade.account_api.post_v1_account_password(
            json=ResetPassword(
                login=login,
                email=email
            )
        )
        return response

    def change_user_email(self, login: str, password: str, email: str):
        response = self.facade.account_api.put_v1_account_email(
            json=ChangeEmail(
                login=login,
                password=password,
                email=email
            )
        )
        return response
