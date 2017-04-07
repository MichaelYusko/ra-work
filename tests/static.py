import pytest
from falcon import testing

from app import create


# Here should collect tests for static resources.


@pytest.fixture(scope='module')
def client():
    return testing.TestClient(create())


def test_home_resource(client):
    result = client.simulate_get('/')
    assert result.status_code == 200
    assert result.json
