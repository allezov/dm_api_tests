from services.dm_api_account import DmApiAccount


def test_put_v1_account_token():
    api = DmApiAccount()
    response = api.account.put_v1_account_token(token='c996510a-df04-4197-9211-9011d620fac0')
    print(response)
