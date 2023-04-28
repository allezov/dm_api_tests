from services.dm_api_account import DmApiAccount


def test_get_v1_account():
    api = DmApiAccount()
    response = api.account.get_v1_account()
    print(response)
