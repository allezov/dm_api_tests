import allure
import pytest

from generic.helpers.orm_db import OrmDatabase
from hamcrest import assert_that, has_properties, has_entries


class AssertionsPostV1Account:
    def __init__(self, db: OrmDatabase):
        self.db = db

    def check_user_was_created(self, result, login, password, status_code, login_check, password_check, email_check):
        if status_code != 201 and len(password) <= 5:
            assert_that(result.json()['errors'], has_entries(
                {
                    'Password': [password_check]
                }
            ))

        elif status_code != 201 and len(login) <= 1:
            assert_that(result.json()['errors'], has_entries(
                {
                    'Login': [login_check]
                }
            ))
        elif status_code != 201:
            assert_that(result.json()['errors'], has_entries(
                {
                    'Email': [email_check]
                }
            ))

        else:
            dataset = self.db.get_user_by_login(login=login)
            for row in dataset:
                assert_that(row, has_properties(
                    {
                        'Login': login,
                        'Activated': False
                    }
                ))
            return True

    def check_user_was_activated(self, login):
        with allure.step('check activate user'):
            dataset = self.db.get_user_by_login(login=login)
            for row in dataset:
                print(row)
                assert_that(row, has_properties(
                    {
                        'Activated': True
                    }
                ))

    def check_user_was_created_for_prepare(self, login):
        with allure.step('check registered new user'):
            dataset = self.db.get_user_by_login(login=login)
            for row in dataset:
                assert_that(row, has_properties(
                    {
                        'Login': login,
                        'Activated': False
                    }
                ))
