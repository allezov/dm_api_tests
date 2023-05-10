from dm_api_account.apis import *


class DmApiAccount:

    def __init__(self, host="http://localhost:5051", headers=None):
        self.login = LoginApi(host, headers)
        self.account = AccountApi(host, headers)


