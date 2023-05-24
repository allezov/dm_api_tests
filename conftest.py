from collections import namedtuple

import pytest
from generic.helpers.mailhog import MailhogApi
from generic.helpers.orm_db import OrmDatabase
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@pytest.fixture
def mailhog():
    return MailhogApi(host="http://localhost:5025")


@pytest.fixture
def dm_api_facade(mailhog):
    return Facade(mailhog=mailhog)


@pytest.fixture
def orm_db():
    return OrmDatabase()


@pytest.fixture
def prepare_user(dm_api_facade, orm_db):
    user_tuple = namedtuple('User', 'login, email, password')

    num = 49
    user = user_tuple(login=f'1test{num}', email=f'test1@test{num}.ru', password='test_password')

    orm_db.delete_user_by_login(login=user.login)
    dataset = orm_db.get_user_by_login(login=user.login)
    assert len(dataset) == 0

    dm_api_facade.mailhog.delete_all_messages()

    return user
