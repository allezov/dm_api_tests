import json
import random
from string import ascii_letters, digits
from collections import namedtuple

import allure
import pytest
from hamcrest import assert_that, has_entries, has_properties


def random_str():
    string = ''
    for i in range(10):
        string += random.choice(ascii_letters + digits)
    return string


def random_invalid_password():
    string = ''
    for i in range(random.randint(1, 5)):
        string += random.choice(ascii_letters + digits)
    return string


def random_valid_password():
    string = ''
    for i in range(random.randint(6, 25)):
        string += random.choice(ascii_letters + digits)
    return string


def random_valid_login():
    string = ''
    for i in range(random.randint(2, 25)):
        string += random.choice(ascii_letters + digits)
    return string


def random_invalid_login():
    string = random.choice(ascii_letters + digits)
    return string


def random_valid_email():
    string = ''
    for i in range(random.randint(1, 10)):
        string += random.choice(ascii_letters + digits)
    return f"{string}@{string}.ru"


def random_invalid_email():
    string = ''
    for i in range(random.randint(1, 10)):
        string += random.choice(ascii_letters + digits)
    return string + '@'


def check_my_symbol(my_str, my_symbol):
    num = sum(1 for i in my_str if i == my_symbol)
    return num


def test_symbol(my_str, my_symbol):
    if my_symbol in my_str:
        return 1


def test_domain_name(my_str='asd@r.ru'):
    if '@.' in my_str:
        return 0


@allure.suite('Тесты на проверку метода POST v1/account')
@allure.sub_suite('Позитивные проверки')
class TestPostV1Account:

    @pytest.mark.parametrize('login, password, email, login_check, password_check,email_check, status_code', [
        (random_valid_login(), random_valid_password(), random_valid_email(), '', '', '', 201),
        (random_valid_login(), random_invalid_password(), random_valid_email(), '', 'Short', '', 400),
        # (random_invalid_login(), random_valid_password(), random_valid_email(), 'Short', '', '', 400),
        # (random_valid_login(), random_valid_password(), random_invalid_email(), '', '', 'Invalid', 400),
        # (random_valid_login(), random_valid_password(), 'login2@test.ru', '', '', 'Taken', 400)
    ])
    def test_create_and_activated_user_with_random_params(
            self,
            dm_api_facade,
            orm_db,
            login,
            password,
            email,
            login_check,
            password_check,
            email_check,
            status_code,
            assertion
    ):
        orm_db.delete_user_by_login(login=login)

        dm_api_facade.mailhog.delete_all_messages()
        result = dm_api_facade.account.register_new_user(login, email, password, status_code)

        print(result)
        print(type(result))
        # print(result.json()['errors'])
        if status_code != 201 and len(password) <= 5:
            assert_that(result.json()['errors'], has_entries(
                {
                    'Password': [password_check]
                }
            ))

            print(result.json()['errors'])
