import os
import unittest

import pytest

from utils.api import Api
from requests import Response


class TestStores(unittest.TestCase):

    def setUp(self):
        self.api = Api()
        self.api.login()

    def test_stores(self):
        self.result: Response = self.api.stores_issue()
        assert 200 == self.result.status_code
        response_json = self.result.json()
        print(response_json)


if __name__ == '__main__':

    pytest.main(args=['-s', os.path.abspath(__file__)])