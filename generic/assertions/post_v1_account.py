from generic.helpers.orm_db import OrmDatabase
from generic.helpers.dm_db import DmDatabase
from hamcrest import assert_that, has_entries


class AssertionsPostV1Account:
    def __init__(self, db: DmDatabase):
        self.db = db

    def check_user_was_created(self, result, login, password, status_code, login_check, password_check, email_check):
        if status_code != 201 and len(password) <= 5:
            print('пароль коротковат')
            assert_that(result.json()['errors'], has_entries(
                {
                    'Password': [password_check]
                }
            ))

        elif status_code != 201 and len(login) <= 1:
            print('логин коротковат')
            assert_that(result.json()['errors'], has_entries(
                {
                    'Login': [login_check]
                }
            ))
        elif status_code != 201:
            print('почта невалидна')
            assert_that(result.json()['errors'], has_entries(
                {
                    'Email': [email_check]
                }
            ))

        else:
            print('похоже все в порядке')
            # Check user in DB
            dataset = self.db.get_user_by_login(login=login)
            for row in dataset:
                assert_that(row, has_entries(
                    {
                        'Login': login,
                        'Activated': False
                    }
                ))
            return True

    def check_user_was_activated(self, login):
        dataset = self.db.get_user_by_login(login=login)
        for row in dataset:
            assert_that(row, has_entries(
                {
                    'Activated': True
                }
            ))

    def check_user_was_created_for_prepare(self, login):
        dataset = self.db.get_user_by_login(login=login)
        for row in dataset:
            assert_that(row, has_entries(
                {
                    'Login': login,
                    'Activated': False
                }
            ))
