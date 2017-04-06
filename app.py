import falcon

from resources.static import StaticResource

api = falcon.API()

api.add_route('/', StaticResource())
