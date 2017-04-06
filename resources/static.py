class StaticResource:
    def on_get(self, req, resp):
        resp.body = """
        Dude, Ra-work will collect your time!
        """
