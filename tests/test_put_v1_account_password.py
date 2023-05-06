from services.dm_api_account import DmApiAccount
from dm_api_account.models.change_password import ChangePassword


def test_put_v1_account_password():
    api = DmApiAccount()
    json = ChangePassword(
        login="<string>",
        token="<uuid>",
        oldPassword="<string>",
        newPassword="<string>"
    )

    response = api.account.put_v1_account_password(json=json)
    print(response)
