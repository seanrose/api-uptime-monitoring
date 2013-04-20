import requests


class APIRequest(object):
    """Handles making API requests"""

    def __init__(self,
                 http_method,
                 url,
                 data=None,
                 params=None,
                 headers=None):

        self.http_method = http_method
        self.url = url
        self.data = data
        self.params = params
        self.headers = headers
        self.elapsed = None

    def __repr__(self):
        return '<{} {} ({} seconds)>'.format(self.http_method.upper(),
                                             self.url,
                                             self.elapsed)

    def make_request(self):
        """Makes the request, updates elapsed time"""

        response = requests.request(self.http_method,
                                    self.url,
                                    data=self.data,
                                    params=self.params,
                                    headers=self.headers)

        self.elapsed = response.elapsed.total_seconds()
        print self.elapsed
