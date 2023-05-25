import time
import random
from string import ascii_letters, digits, ascii_lowercase
from collections import namedtuple
import pytest
from hamcrest import assert_that, has_entries


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
    return string


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


@pytest.mark.parametrize('login, password, email, login_check, password_check,email_check, status_code', [
    (random_valid_login(), random_valid_password(), random_valid_email(), '', '', '', 201),
    (random_valid_login(), random_invalid_password(), random_valid_email(), '', 'Short', '', 400),
    # (random_valid_login(), random_valid_password(), random_valid_email(), '', '', '', 201),
    (random_invalid_login(), random_valid_password(), random_valid_email(), 'Short', '', '', 400),
    # (random_valid_login(), random_valid_password(), random_valid_email(), '', '', '', 201),
    (random_valid_login(), random_valid_password(), random_invalid_email(), '', '', 'Invalid', 400),
    (random_valid_login(), random_valid_password(), 'login2@test.ru', '', '', 'Taken', 400)
])
def test_post_v1_account_1(dm_api_facade, orm_db, login, password, email, login_check, password_check, email_check,
                           status_code):
    # orm_db.delete_user_by_email(email=email)
    orm_db.delete_user_by_login(login=login)
    if status_code == 201:
        dm_api_facade.mailhog.delete_all_messages()
    # Register new user
    result = dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=status_code
    )
    # assert password
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
            } or
            {
                'Email': [email_check]
            }
        ))

    else:
        # Check user in DB
        dataset = orm_db.get_user_by_login(login=login)
        for row in dataset:
            assert_that(row, has_entries(
                {
                    'Login': login,
                    'Activated': False
                }
            ))

        # Get token and activate user
        dm_api_facade.account.activate_registered_user(login=login)
        time.sleep(2)

        # Check user in DB for check activation
        dataset = orm_db.get_user_by_login(login=login)
        for row in dataset:
            assert_that(row, has_entries(
                {
                    'Activated': True
                }
            ))

        # Login user
        dm_api_facade.login.login_user(
            login=login,
            password=password
        )


def test_post_v1_account_2(dm_api_facade, orm_db, prepare_user):
    # Prepare user
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    orm_db.delete_user_by_login(login=login)

    # Register new user
    result = dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    # Check user in DB
    dataset = orm_db.get_user_by_login(login=login)
    for row in dataset:
        assert_that(row, has_entries(
            {
                'Login': login,
                'Activated': False
            }
        ))

    # Get token and activate user
    dm_api_facade.account.activate_registered_user(login=login)
    time.sleep(2)

    # Check user in DB for check activation
    dataset = orm_db.get_user_by_login(login=login)
    for row in dataset:
        assert_that(row, has_entries(
            {
                'Activated': True
            }
        ))

    # Login user
    dm_api_facade.login.login_user(
        login=login,
        password=password
    )
