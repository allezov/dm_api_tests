from services.dm_api_account import Facade


def test_user_behave_1():
    api = Facade()
    # Register new user
    num = 39
    login = f'1test{num}'
    email = f'test1@test{num}.ru'
    password = 'test_password'

    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    # Activate new user
    api.account.activate_registered_user(login=login)

    # Login user + get token

    api.login.login_user(
        login=login,
        password=password
    )
    token = api.login.get_auth_token(login=f'1test{num}', password='test_password')

    # first_example_logout
    # api.login.logout_user(headers=token)

    # second_example_logout
    api.login.set_headers(headers=token)
    api.login.logout_user()
