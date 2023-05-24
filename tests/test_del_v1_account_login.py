def test_del_v1_account_login(dm_api_facade):
    response = dm_api_facade.login_api.del_v1_account_login()
    print(response)
