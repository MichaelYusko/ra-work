import pytest
from falcon.testing import TestClient

from app import api

test_client_api = TestClient(api)


@pytest.fixture(scope='function')
def client_app():
    return test_client_api
