import falcon
import pytest

from models import AnonymousUser
from utils.permission import is_authenticated, is_employee, is_manager


def test_permission():
    class Req:
        context = {'user': AnonymousUser()}

    req = Req()

    with pytest.raises(falcon.HTTPUnauthorized):
        is_authenticated(req, None, None, None)

    with pytest.raises(falcon.HTTPUnauthorized):
        is_manager(req, None, None, None)

    with pytest.raises(falcon.HTTPUnauthorized):
        is_employee(req, None, None, None)
