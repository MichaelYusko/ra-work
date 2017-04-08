import falcon

from models import UserRole

TITLE = 'Authentication required'
DESCRIPTION = 'Please provide an auth token as part of the request.'
CHALLENGES = None


def is_authenticated(req, resp, resource, params):
    user = req.context['user']
    if not user.is_authenticated():
        raise falcon.HTTPUnauthorized(TITLE, DESCRIPTION, CHALLENGES)


def is_manager(req, resp, resource, params):
    user = req.context['user']
    if not (user.is_authenticated() and user.role == UserRole.MANAGER.value):
        raise falcon.HTTPUnauthorized(TITLE, DESCRIPTION, CHALLENGES)


def is_employee(req, resp, resource, params):
    user = req.context['user']
    if not (user.is_authenticated() and user.role == UserRole.EMPLOYEE.value):
        raise falcon.HTTPUnauthorized(TITLE, DESCRIPTION, CHALLENGES)
