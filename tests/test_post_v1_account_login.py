def test_post_v1_account_login(dm_api_facade):
    return dm_api_facade.login.login_user(login='1test37', password='test_password')
