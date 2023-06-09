from data.post_v1_account import PostV1Account as user_data


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

    token = mailhog.get_token_by_login(login=login)
    print(token)

    # Не понимаю почему token - invalid
    dm_api_facade.account.change_user_password(login=login, token=token, old_password=password,
                                               new_password=new_password)

    # dm_api_facade.login.login_user(login=login, password=new_password)
    # orm_db.delete_user_by_login(login=login)
