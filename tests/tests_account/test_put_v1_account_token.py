from hamcrest import assert_that, has_properties
from apis.dm_api_account.models.user_envelope import UserRole


def test_put_v1_account_token(dm_api_facade):
    response = dm_api_facade.account_api.put_v1_account_token(token='ba82b3b8-1831-4c83-b02c-ebe0c6edadab',
                                                              status_code=200)
    assert_that(response.resource, has_properties(
        {
            'login': "1test19",
            'roles': [UserRole.guest, UserRole.player]
        }
    ))
