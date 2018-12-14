import requests

from api_tests.params import Json, Header, Urls


class Login:

    @staticmethod
    def login_manager():
        return requests.request('POST', Urls.url,
                                json=Json.params_login_manager, headers=Header.header).cookies
