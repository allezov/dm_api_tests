from services.dm_api_account import Facade
from dm_api_account.models.reset_password import ResetPassword


def test_post_v1_account_password():
    api = Facade()
    json = ResetPassword(
        login="str",
        email="str"
    )
    response = api.account_api.post_v1_account_password(json=json)
    print(response)
    print(response.url)
