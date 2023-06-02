def test_put_v1_account_email(dm_api_facade):
    response = dm_api_facade.account.change_user_email(login='1test49', password='test_password',
                                                       email='test1@test49.ru')
    print(response)
