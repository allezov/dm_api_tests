from services.dm_api_account import DmApiAccount


def test_post_v1_account_password():
    api = DmApiAccount()
    json = {
        "login": "<string>",
        "email": "<string>"
    }
    response = api.account.post_v1_account_password(json=json)
    print(response)
    print(response.url)
