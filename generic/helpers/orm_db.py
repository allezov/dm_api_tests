from typing import List
from sqlalchemy import select, delete, update
from generic.helpers.orm_models import User
from orm_client.orm_client import OrmClient


class OrmDatabase:
    def __init__(self):
        self.orm = OrmClient()
        pass

    def get_user_by_login(self, login) -> List[User]:
        query = select([User]).where(User.Login == login)
        return self.orm.send_query(query=query)

    def get_all_users(self):
        query = select([User])
        return self.orm.send_query(query=query)

    def delete_user_by_login(self, login):
        query = delete(User).where(User.Login == login)
        print(query)
        return self.orm.send_bulk_query(query=query)

    def activate_user_by_db(self, login):
        query = update(User).values({User.Activated: True}).where(User.Login == login)
        return self.orm.send_bulk_query(query=query)
