from services.dm_api_account import Facade
from dm_api_account.models.change_password import ChangePassword


def test_put_v1_account_password():
    api = Facade()
    json = ChangePassword(
        login="<string>",
        token="<uuid>",
        oldPassword="<string>",
        newPassword="<string>"
    )

    response = api.account_api.put_v1_account_password(json=json)
    print(response)
