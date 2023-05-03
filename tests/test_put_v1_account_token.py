from services.dm_api_account import DmApiAccount


def test_put_v1_account_token():
    api = DmApiAccount()
    response = api.account.put_v1_account_token()
    print(response)
