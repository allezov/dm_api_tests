def test_get_v1_account(dm_api_facade):
    token = dm_api_facade.login.get_auth_token(login='1test49', password='test_password')
    dm_api_facade.account.set_headers(headers=token)
    dm_api_facade.login.set_headers(headers=token)

    dm_api_facade.account.get_current_user()
    dm_api_facade.login.logout_user()
