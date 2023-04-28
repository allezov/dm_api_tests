from services.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount()
    json = {
        "login": "<test14>",
        "email": "<test14@test.ru>",
        "password": "<testtest14>"
    }
    response = api.account.post_v1_account(json=json)
    print(response)

