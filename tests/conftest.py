import pytest
from app import api
from falcon.testing import TestClient


test_client_api = TestClient(api)


@pytest.fixture(scope='function')
def client_app():
    return test_client_api
