from generic.helpers.orm_db import OrmDatabase
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_orm():
    orm = OrmDatabase()
    # dataset = orm.get_all_users()
    dataset = orm.get_user_by_login('1test49')
    for row in dataset:
        print(row.Login)
    orm.orm.close_connection()
