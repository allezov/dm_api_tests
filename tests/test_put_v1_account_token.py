import structlog
from hamcrest import assert_that, has_properties
from services.dm_api_account import Facade
from dm_api_account.models.user_envelope import UserRole

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = Facade()
    response = api.account_api.put_v1_account_token(token='ba82b3b8-1831-4c83-b02c-ebe0c6edadab', status_code=200)
    assert_that(response.resource, has_properties(
        {
            'login': "1test19",
            'roles': [UserRole.guest, UserRole.player]
        }
    ))
