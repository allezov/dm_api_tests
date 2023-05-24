import time
import random
from string import ascii_letters, digits, ascii_lowercase

import pytest
from hamcrest import assert_that, has_entries


def random_str():
    string = ''
    for i in range(10):
        string += random.choice(ascii_letters + digits)
    return string


def random_len_str():
    my_str = ''
    count = random.choice([3, 4, 5, 6, 7, 8, 9, 10])
    for i in range(count):
        my_str += random.choice(ascii_letters + digits)
    return my_str


def random_email():
    test = '@@@@@@@@@@$!'
    string = ''
    for i in range(10):
        string += random.choice(ascii_letters + test)
    return string


def sum_upper_symbols(my_str):
    count = sum(1 for i in my_str if i.isupper())
    return count


def check_my_symbol(my_str, my_symbol):
    num = sum(1 for i in my_str if i == my_symbol)
    return num


# @pytest.mark.parametrize('password, password_check', [(random_len_str(), 6)])
# @pytest.mark.parametrize('email, email_check', [(random_str() + '@' + random_str() + '.ru' for i in range(2)), '@'])
@pytest.mark.parametrize('login, login_check', [(random_str(), sum_upper_symbols(random_str()))])
@pytest.mark.parametrize('email, email_check', [(random_str() + '@' + random_str() + '.ru', '@')])
@pytest.mark.parametrize('password, password_check', [(random_len_str(), 6)])
def test_post_v1_account(dm_api_facade, orm_db, login, password, email, login_check, password_check, email_check):
    orm_db.delete_user_by_login(login=login)
    dm_api_facade.mailhog.delete_all_messages()
    # Prepare user
    # login = prepare_user.login
    # password = prepare_user.password
    # email = prepare_user.email

    assert login_check >= 1, 'need at least 1 capital letter'
    assert len(password) >= password_check, f"password must be more than{password_check} symbols"
    assert check_my_symbol(email, email_check) == 1, 'there must be 1 character "@"'
    # Register new user
    dm_api_facade.account.register_new_user(
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
