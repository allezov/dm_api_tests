from services.dm_api_account import Facade


def test_get_v1_account():
    api = Facade()
    token = api.login.get_auth_token(login='1test36', password='test_password')
    api.account.set_headers(headers=token)
    api.login.set_headers(headers=token)

    api.account.get_current_user()
    api.login.logout_user()
