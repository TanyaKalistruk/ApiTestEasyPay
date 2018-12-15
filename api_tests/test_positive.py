import allure
import requests

from api_tests import db_checking
from api_tests.params import Urls, Json, Par
from api_tests.login import Login


def test_change_price():
    cookie_login = Login.login_manager()
    status = requests.request('PUT', Urls.url_update_price,
                              json=Json.update_price, cookies=cookie_login)
    with allure.step('It is valid price'):
        assert 200 <= status.status_code < 300
    with allure.step('Db updated'):
        assert db_checking.new_price() == 1


def test_delete_inspector():
    cookie_login = Login.login_manager()
    status = requests.request('DELETE', Urls.url_delete_inspector,
                              json=Par.inspector_id, cookies=cookie_login)
    with allure.step('It is valid id for inspector'):
        assert 200 <= status.status_code < 300
    with allure.step('Db updated'):
        assert db_checking.present_inspector() == 0


def test_add_inspector():
    if db_checking.present_inspector() == 0:
        cookie_login = Login.login_manager()
        status = requests.request('PUT', Urls.url_add_inspector,
                                  json=Par.id_add, cookies=cookie_login)
        with allure.step('It is valid id for inspector'):
            assert 200 <= status.status_code < 300
        with allure.step('Db updated'):
            assert db_checking.present_inspector() == 1
