from services.dm_api_account import Facade


def test_post_v1_account_login():
    api = Facade()
    response = api.login.login_user(login='1test37', password='test_password')
    return response


