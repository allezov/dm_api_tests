from generic.helpers.dm_db import DmDatabase
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_db():
    activate = Facade()
    db = DmDatabase(user='postgres', password='admin', host='localhost', database='dm3.5')

    login = '1test49'

    db.activate_user_by_db(login=login)
    activate.account.activate_registered_user(login=login)

