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



