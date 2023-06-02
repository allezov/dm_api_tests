def test_post_v1_account_password(dm_api_facade):
    response = dm_api_facade.account.reset_user_password(login='1test49', email='test1@test49.ru')
    print(response)
    print(response.url)
