import falcon


class MediaTyperMiddleware:
    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable(
                'Ra-work API only supports responses encoded as JSON'
            )

        if req.method in ('POST', 'PUT', 'PATCH'):
            ct = req.content_type
            if (ct and 'application/json' not in ct) or not ct:
                raise falcon.HTTPUnsupportedMediaType(
                    'Ra-work API supports requests encoded as JSON.'
                )
