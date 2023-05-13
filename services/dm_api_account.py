from generic.helpers.account import Account
from generic.helpers.login import Login
from generic.helpers.mailhog import MailhogApi
from dm_api_account.apis import AccountApi
from dm_api_account.apis import LoginApi


class Facade:

    def __init__(self, host="http://localhost:5051", mailhog_host=None, headers=None):
        self.login_api = LoginApi(host, headers)
        self.account_api = AccountApi(host, headers)
        self.mailhog = MailhogApi()
        self.account = Account(self)
        self.login = Login(self)
