import json


class StaticResource:
    def on_get(self, req, resp):
        text = {
            'User': 'Ra-worker',
            'Text': 'Dude, I will collect your time!'
        }
        resp.body = json.dumps(text)
