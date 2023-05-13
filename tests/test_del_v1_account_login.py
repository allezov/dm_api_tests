from services.dm_api_account import Facade


def test_del_v1_account_login():
    api = Facade()
    response = api.login_api.del_v1_account_login()
    print(response)
