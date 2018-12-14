import requests
import allure

from api_tests.params import Urls, Json
from api_tests.db import DBConnection
from api_tests.login import Login


def test_change_price():
    cookie_login = Login.login_manager()
    status = requests.request('PUT', Urls.url_update_price,
                              json=Json.negative_update_price, cookies=cookie_login)
    with allure.step('It is not valid price'):
        assert 200 > status.status_code or status.status_code >= 300


def test_delete_inspector():
    with DBConnection() as db:
        if db.check_delete_inspector() != 0:
            cookie_login = Login.login_manager()
            string = "qwerty"
            status = requests.request('DELETE', Urls.url_delete_inspector,
                                      json=string, cookies=cookie_login)
            with allure.step('It is not valid id for inspector'):
                assert 200 > status.status_code or status.status_code >= 300


def test_add_inspector():
    with DBConnection() as db:
        if db.check_delete_inspector() == 0:
            cookie_login = Login.login_manager()
            string = "qwerty"
            status = requests.request('PUT', Urls.url_add_inspector,
                                      json=string, cookies=cookie_login)
            with allure.step('It is not valid id for inspector'):
                assert 200 > status.status_code or status.status_code >= 300
