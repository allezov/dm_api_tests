def test_db(dm_api_facade, orm_db):
    # activate = Facade()
    num = 49
    login = f'1test{num}'
    email = f'test1@test{num}.ru'
    password = 'test_password'

    # orm = OrmDatabase()
    orm_db.delete_user_by_login(login=login)

    dm_api_facade.mailhog.delete_all_messages()

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    orm_db.activate_user_by_db(login=login)

    dm_api_facade.account.activate_registered_user(login=login)

    orm_db.orm.close_connection()
