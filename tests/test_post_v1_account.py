from services.dm_api_account import Facade
import structlog
import time
from dm_api_account.models.registration_module import Registration

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    api = Facade()
    # Register new user
    num = 43
    login = f'1test{num}'
    email = f'test1@test{num}.ru'
    password = 'test_password'

    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    # Get token
    api.account.activate_registered_user(login=login)

    # # # Login user
    api.login.login_user(
        login=login,
        password=password
    )
