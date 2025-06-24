import asyncio
from abc import ABC

import aiohttp

from logger_settings import logger as log

class SESSION(ABC):
    def __init__(self, timeout: int = 15):
        self.headers = {
            "Content-Type": "application/json",
            "accept": "application/json"
        }
        self.timeout = timeout

class GUERRML(SESSION):
    def __init__(self):
        super().__init__()

    async def request_(self, url: str, method: str, **kwargs):
        try:
            payload = {**kwargs}

            async with aiohttp.ClientSession() as session:
                async with session.request(method=method, url=url, json=payload, headers=self.headers) as res:
                    if res.status == 200:
                        return await res.json()
                    else:
                        raise Exception(f"Error request: {res.status} — {await res.text()}")

        except Exception as err:
            log.error(
                "An error occurred in the "
                f"block GUERRML.request_: {err}"
            )
            return False