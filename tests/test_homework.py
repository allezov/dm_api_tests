def test_user_behave_1(dm_api_facade):
    # Register new user
    num = 45
    login = f'1test{num}'
    email = f'test1@test{num}.ru'
    password = 'test_password'

    response = dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    # Activate new user
    dm_api_facade.account.activate_registered_user(login=login)

    # Login user + get token

    dm_api_facade.login.login_user(
        login=login,
        password=password
    )
    token = dm_api_facade.login.get_auth_token(login=f'1test{num}', password='test_password')

    # first_example_logout
    dm_api_facade.login.logout_user(headers=token)

    # # second_example_logout
    # dm_api_facade.login.set_headers(headers=token)
    # dm_api_facade.login.logout_user()
