import time

from generic.helpers.dm_db import DmDatabase
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    api = Facade()
    # Register new user
    num = 49
    login = f'1test{num}'
    email = f'test1@test{num}.ru'
    password = 'test_password'

    db = DmDatabase(user='postgres', password='admin', host='localhost', database='dm3.5')
    db.delete_user_by_login(login=login)
    dataset = db.get_user_by_login(login=login)
    print('dataset = ', dataset)
    assert len(dataset) == 0

    api.mailhog.delete_all_messages()

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Login'] == login, f"User{login} not registered"
        assert row['Activated'] is False, f"User{login} was activated"

    # Get token
    api.account.activate_registered_user(login=login)
    time.sleep(4)
    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Activated'] is True, f"User{login} not activated"

    # Login user
    api.login.login_user(
        login=login,
        password=password
    )
