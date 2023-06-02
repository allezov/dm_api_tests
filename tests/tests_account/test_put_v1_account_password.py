from apis.dm_api_account.models.change_password import ChangePassword


def test_put_v1_account_password(dm_api_facade):
    json = ChangePassword(
        login="<string>",
        token="<uuid>",
        oldPassword="<string>",
        newPassword="<string>"
    )

    response = dm_api_facade.account_api.put_v1_account_password(json=json)
    print(response)
