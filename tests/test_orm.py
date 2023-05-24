def test_orm(orm_db):
    # dataset = orm.get_all_users()
    dataset = orm_db.get_user_by_login('1test49')
    for row in dataset:
        print(row.Login)
    orm_db.orm.close_connection()
