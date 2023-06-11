import time


def test_put_v1_account_password(dm_api_facade, mailhog, orm_db, prepare_user):
    login = prepare_user.login
    password = prepare_user.password
    new_password = prepare_user.new_password
    email = prepare_user.email

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
    )
    dm_api_facade.account.activate_registered_user(login=login)

    dm_api_facade.account.reset_user_password(login=login, email=email)
    time.sleep(2)

    token = mailhog.get_token_from_last_email()
    print(token)

    response = dm_api_facade.login.login_user(login=login, password=new_password)

    print(response)

    # dm_api_facade.account.change_user_password(login=login, token=token, old_password=password,
    #                                            new_password=new_password)


    # orm_db.delete_user_by_login(login=login)
