# Here should collect tests for static resources.
def test_home_resource(client_app):
    result = client_app.simulate_get('/')
    assert result.status_code == 200
    assert result.json
