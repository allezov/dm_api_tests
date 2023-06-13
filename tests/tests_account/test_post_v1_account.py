import random
from string import ascii_letters, digits
from collections import namedtuple
from data.post_v1_account import PostV1Account as user_data
import allure
import pytest
from generic.assertions.response_checker import check_status_code_http


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


def test_domain_name(my_str='asd@r.ru'):
    if '@.' in my_str:
        return 0


@allure.suite('Тесты на проверку метода POST v1/account')
@allure.sub_suite('Позитивные проверки')
class TestPostV1Account:
    input_data = [
        (random_valid_login(), random_valid_password(), random_valid_email(), 201, ''),
        (random_valid_login(), random_invalid_password(), random_valid_email(), 400, {"Password": ["Short"]}),
        (random_invalid_login(), random_valid_password(), random_valid_email(), 400, {"Login": ["Short"]}),
        (random_valid_login(), random_valid_password(), random_invalid_email(), 400, {"Email": ["Invalid"]}),
        (random_valid_login(), random_valid_password(), 'test1@test49.ru', 400, {"Email": ["Taken"]}),
    ]

    @pytest.mark.parametrize('login, password, email, status_code, check', input_data)
    def test_create_and_activated_user_with_random_params(
            self,
            dm_api_facade,
            orm_db,
            login,
            password,
            email,
            check,
            status_code,
            assertion
    ):
        orm_db.delete_user_by_login(login=login)
        dm_api_facade.mailhog.delete_all_messages()
        with check_status_code_http(expected_status_code=status_code, expected_result=check):
            dm_api_facade.account.register_new_user(login, email, password)

        if status_code == 201:
            assertion.check_user_was_created_for_prepare(login=login)
            dm_api_facade.account.activate_registered_user(login=login)
            assertion.check_user_was_activated(login=login)
            dm_api_facade.login.login_user(
                login=login,
                password=password
            )

    @allure.title('Проверка создания и активация через "prepare_user"')
    @allure.step('проверка')
    def test_create_and_activated_user_with_prepare_params(self, dm_api_facade, orm_db, prepare_user, assertion):
        login = prepare_user.login
        password = prepare_user.password
        email = prepare_user.email
        orm_db.delete_user_by_login(login=login)
        dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password,
        )
        assertion.check_user_was_created_for_prepare(login=login)
        dm_api_facade.account.activate_registered_user(login=login)
        assertion.check_user_was_activated(login=login)
        dm_api_facade.login.login_user(login=login, password=password)
