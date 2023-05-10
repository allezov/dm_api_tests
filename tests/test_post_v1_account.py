from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.registration_module import Registration

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = MailhogApi(host="http://localhost:5025")
    api = DmApiAccount(host="http://localhost:5051")
    json = Registration(
        login="1test21",
        email="test1@test21.ru",
        password="12345678"
    )

    response = api.account.post_v1_account(json=json)

    # token = mailhog.get_token_from_last_email()
    # result = api.account.put_v1_account_token(token=token)
