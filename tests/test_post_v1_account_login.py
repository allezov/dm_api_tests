from services.dm_api_account import DmApiAccount
from dm_api_account.models.login_credentials import LoginCredentials


def test_post_v1_account_login():
    api = DmApiAccount()
    json = LoginCredentials(
        login="<string>",
        password="<string>",
        rememberMe=bool
    )

    response = api.login.post_v1_account_login(json=json)
    print(response)
