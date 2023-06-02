import random
from string import ascii_letters, digits
from collections import namedtuple
from data.post_v1_account import PostV1Account as user_data
import allure
import pytest


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
    # @pytest.mark.parametrize('login, password, email, check, status_code', [
    #     (random_valid_login(), random_valid_password(), random_valid_email(), '', 201),
    #     (random_valid_login(), random_invalid_password(), random_valid_email(), 'Shrt', 400),
    #     (random_invalid_login(), random_valid_password(), random_valid_email(), 'Short', 400),
    #     (random_valid_login(), random_valid_password(), random_invalid_email(), 'Invalid', 400),
    #     (random_valid_login(), random_valid_password(), 'test1test36.ru', 'Invalid', 400)
    # ])

    @pytest.mark.parametrize('login, password, email, login_check, password_check,email_check, status_code', [
        (random_valid_login(), random_valid_password(), random_valid_email(), '', '', '', 201),
        (random_valid_login(), random_invalid_password(), random_valid_email(), '', 'Short', '', 400),
        (random_invalid_login(), random_valid_password(), random_valid_email(), 'Short', '', '', 400),
        (random_valid_login(), random_valid_password(), random_invalid_email(), '', '', 'Invalid', 400),
        (random_valid_login(), random_valid_password(), 'login2@test.ru', '', '', 'Taken', 400)
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
        check_assert = assertion.check_user_was_created(
            result=result,
            login=login,
            password=password,
            status_code=status_code,
            login_check=login_check,
            password_check=password_check,
            email_check=email_check
        )
        if check_assert:
            dm_api_facade.account.activate_registered_user(login=login)
            assertion.check_user_was_activated(login=login)
            dm_api_facade.login.login_user(
                login=login,
                password=password
            )

    @allure.step('подготовка тестового пользователя')
    @pytest.fixture
    def prepare_user(self, dm_api_facade, orm_db):
        user_tuple = namedtuple('User', 'login, email, password')
        user = user_tuple(
            login=user_data.login,
            password=user_data.password,
            email=user_data.email
        )
        orm_db.delete_user_by_login(login=user.login)
        dataset = orm_db.get_user_by_login(login=user.login)
        assert len(dataset) == 0
        dm_api_facade.mailhog.delete_all_messages()
        return user

    @allure.title('Проверка создания и активация через "prepare_user"')
    @allure.step('проверка')
    def test_create_and_activated_user_with_prepare_params(self, dm_api_facade, orm_db, prepare_user, assertion,
                                                           status_code=201):
        login = prepare_user.login
        password = prepare_user.password
        email = prepare_user.email
        orm_db.delete_user_by_login(login=login)
        dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password,
            status_code=status_code
        )
        assertion.check_user_was_created_for_prepare(login=login)
        dm_api_facade.account.activate_registered_user(login=login)
        assertion.check_user_was_activated(login=login)
        dm_api_facade.login.login_user(login=login, password=password)
