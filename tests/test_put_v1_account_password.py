from services.dm_api_account import DmApiAccount


def test_put_v1_account_password():
    api = DmApiAccount()
    json = {
        "login": "<string>",
        "token": "<uuid>",
        "oldPassword": "<string>",
        "newPassword": "<string>"
    }
    response = api.account.put_v1_account_password(json=json)
    print(response)
