import falcon

from middleware.json import MediaTyperMiddleware
from resources.static import StaticResource

# Middleware
middleware = [MediaTyperMiddleware()]

api = falcon.API(middleware=middleware)


# Routes
api.add_route('/', StaticResource())
