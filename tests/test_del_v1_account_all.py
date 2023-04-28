from services.dm_api_account import DmApiAccount


def test_del_v1_account_all():
    api = DmApiAccount()
    response = api.login.del_v1_account_all()
    print(response)
    print(response.url)

