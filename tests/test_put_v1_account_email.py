from services.dm_api_account import Facade
from dm_api_account.models.change_email import ChangeEmail


def test_put_v1_account_email():
    api = Facade()
    json = ChangeEmail(
        login="<string>",
        password="<string>",
        email="<string>"
    )
    response = api.account_api.put_v1_account_email(json=json)
    print(response)
