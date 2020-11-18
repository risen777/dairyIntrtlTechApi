import logging
import json
import os

from allure_commons._allure import step
from utils.constants import Constants
from utils.http_manager import HttpManager


class Api:
    working_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = working_directory + '\\config.json'
    LOGGER = logging.getLogger(__name__)
    with open(file_path, 'r') as f:
        data = json.load(f)
        # json_string = str(json.dumps(data))
    token = ""

    @staticmethod
    def login():
        with step("Login"):
            # user_name = Api.data["login"]
            # password = Api.data["password"]
            result = HttpManager.auth(Constants.LOGIN_ISSUE, Api.data)

            response_json = result.json()

            Api.token = response_json["token"]
            assert Api.token is not None
# Api.LOGGER.info('TEST: Login with {0}, {1} credentials'.format())
            assert 200 == result.status_code

    @staticmethod
    def stores_issue():
        with step("Stores"):
         result = HttpManager.get(Constants.STORES_ISSUE,
                                 Api.token)
         # Api.LOGGER.info('TEST: Create issue. Method: {0}, Data: {1}'.format("GET", result))
        return result
