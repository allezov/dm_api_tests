from services.dm_api_account import DmApiAccount
from dm_api_account.models.change_email import ChangeEmail


def test_put_v1_account_email():
    api = DmApiAccount()
    json = ChangeEmail(
        login="<string>",
        password="<string>",
        email="<string>"
    )
    response = api.account.put_v1_account_email(json=json)
    print(response)
