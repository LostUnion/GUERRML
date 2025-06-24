from abc import ABC
from typing import *

from curl_cffi import requests

from logger_settings import logger as log

class CONFIG(ABC):
    def __init__(self, timeout: int = 15):
        self.session = requests.Session()
        self.url = 'http://api.guerrillamail.com/ajax.php'
        self.ip = '127.0.0.1',
        self.agent='GuerrillaMailPythonClient/1.0'
        self.headers = {'User-Agent': f'{self.agent}'}
        self.lang = 'en'
        self.phpsessid = None
        self.cookies = {}
        self.timeout = timeout

class GUERRML(CONFIG):
    def __init__(self):
        super().__init__()

    def request_(self, method: str, func: str, **kwargs):
        try:
            params = {
                'f': func,
                'ip': self.ip,
                'lang': self.lang,
                'agent': self.agent,
                **kwargs
            }

            if self.phpsessid:
                self.cookies['PHPSESSID'] = self.phpsessid

            http_method = getattr(self.session, method.lower())

            res = http_method(
                url=self.url,
                params=params,
                headers=self.headers
            )

            if "PHPSESSID" in res.cookies:
                self.phpsessid = res.cookies['PHPSESSID']

            return res.json()

        except Exception as err:
            log.error(
                f"An error occurred in the block GUERRML.request_: {err}"
            )
            return False
        
    def get_email_address(self):
        """Returns random mail with a domain guerrillamailblock.com."""
        try:
            res = self.request_(method='GET', func=self.get_email_address.__name__).get('email_addr')
            return res if res else False
        except Exception as err:
            log.error(
                f"An error occurred in the block GUERRML.get_email_address: {err}"
            )
            return False


service = GUERRML()      
print(service.get_email_address())