import json
import logging
import token

import requests


class HttpManager:
    header = {'Content-Type': 'application/json'}
    LOGGER = logging.getLogger(__name__)
    @staticmethod
    def auth(url, body):
        result = requests.post(url, json=body, headers=HttpManager.header)
        print(result)
        return result



    @staticmethod
    def get(url,token):
        header = {'Authorization': 'Bearer ' + token}
        result = requests.get(url,
                               headers=header)
        print(result)
        return result

    @staticmethod
    def post(url,token, body):
        header = {'Authorization': 'Bearer ' + token}
        result = requests.post(url,
                               json=body,
                               headers=header)
        print(result)
        return result

