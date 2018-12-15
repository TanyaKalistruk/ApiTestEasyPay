from api_tests.db import DBConnection


def present_inspector():
    with DBConnection() as db:
        return db.check_delete_inspector()


def new_price():
    with DBConnection() as db:
        return db.check_price()
