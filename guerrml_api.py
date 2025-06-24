import re
import time
import random
from abc import ABC
from typing import *

from curl_cffi import requests

from usergen import USERGEN
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

    def __request(self, method: str, func: str, **kwargs):
        try:
            params = {
                'f': func,
                'ip': self.ip,
                'lang': self.lang,
                'agent': self.agent,
                **kwargs,
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
            res = self.__request(method='GET', func=self.get_email_address.__name__).get('email_addr')
            return res if res else False
        except Exception as err:
            log.error(
                f"An error occurred in the block GUERRML.get_email_address: {err}"
            )
            return False
        
    def __email_gen(self, username):
        try:
            def variant_1(username):
                return re.sub(r'(?<!^)(?=[A-Z])', '_', username)
            
            def variant_2(username):
                return re.sub(r'(?<=\D)(?=\d)', '_', username)
            
            def variant_3(username):
                user_email = re.sub(r'(?<!^)(?=[A-Z])', '_', username)
                user_email = re.sub(r'(?<=\D)(?=\d)', '_', user_email)
                return user_email
            
            def variant_4(username):
                return re.sub(r'(?<!^)(?=[A-Z])', '.', username)
            
            def variant_5(username):
                return re.sub(r'(?<=\D)(?=\d)', '.', username)
            
            def variant_6(username):
                user_email = re.sub(r'(?<!^)(?=[A-Z])', '.', username)
                user_email = re.sub(r'(?<=\D)(?=\d)', '.', user_email)
                return user_email
            
            def variant_7(username):
                user_email = re.sub(r'(?<!^)(?=[A-Z])', '_', username)
                user_email = re.sub(r'(?<=\D)(?=\d)', '.', user_email)
                return user_email
            
            def variant_8(username):
                user_email = re.sub(r'(?<!^)(?=[A-Z])', '_', username)
                user_email = re.sub(r'(?<=\D)(?=\d)', '.', user_email)
                return user_email

            user_email = random.choice([
                variant_1(username), variant_2(username),
                variant_3(username), variant_4(username),
                variant_5(username), variant_6(username),
                variant_7(username), variant_8(username)
            ])
            
            return user_email.lower()

        except Exception as err:
            log.error(
                    "Ошибка в блоке Reger."
                    f"email_gen: {err}"
                )

            return False
        
    def set_email_user(self):
        """Replacing the default username in the email address."""
        try:
            username = USERGEN().get_username()
            new_email = self.__email_gen(username)
            res = self.__request(method='GET', func=self.set_email_user.__name__, email_user=new_email).get('email_addr')
            return res if res else False
        except Exception as err:
            log.error(
                f"An error occurred in the block GUERRML.set_email_user: {err}"
            )
            return False
        
    def check_email(self, seq: int = 0):
        """Checking for new emails."""
        try:
            # time.sleep(3)
            res = self.__request(method='GET', func=self.check_email.__name__, seq=seq).get('list')[0]
            mail_from = res.get('mail_from')
            # if mail_from in ['no-reply@guerrillamail.com']:
                # mail_id = res.get('mail_id')
                # success = self.del_email([mail_id])
                # log.info('Service message deleted!')
                # return success if success else False

            return res if res else False
        except Exception as err:
            log.error(
                f"An error occurred in the block GUERRML.check_email: {err}"
            )
            return False
        
    def del_email(self, email_ids: list):
        """Deleting an email from the mail."""
        try:
            res = self.__request(method='GET', func=self.del_email.__name__, **{"email_ids[]": email_ids}).get('auth').get('success')
            return res if res else False
        except Exception as err:
            log.error(
                f"An error occurred in the block GUERRML.del_email: {err}"
            )
            return False
        
    def fetch_email(self, email_id: int):
        """Viewing the contents of an email."""
        try:
            res = self.__request(method='GET', func=self.fetch_email.__name__, email_id=email_id)
            return res if res else False
        except Exception as err:
            log.error(
                f"An error occurred in the block GUERRML.fetch_email: {err}"
            )
            return False

