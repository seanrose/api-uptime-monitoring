from db_session import Base, load_session
import requests


class APIRequestModel(Base):
    """"""
    __tablename__ = 'responses'
    __table_args__ = {'autoload': True}


def fetch_requests():

    return {}


class APIRequest(object):
    """Handles making API requests"""

    def __init__(self,
                 id=None,
                 http_method=None,
                 url=None,
                 data=None,
                 params=None,
                 headers=None):

        self.http_method = http_method
        self.url = url
        self.data = data or {}
        self.params = params or {}
        self.headers = headers or {}
        self.elapsed = None

    def __repr__(self):
        return '<{} {} ({} seconds)>'.format(self.http_method.upper(),
                                             self.url)

    def make_request(self):
        """Makes the request, updates elapsed time"""

        response = requests.request(self.http_method,
                                    self.url,
                                    data=self.data,
                                    params=self.params,
                                    headers=self.headers)

        self.elapsed = response.elapsed.total_seconds()

    def save_request(self):
        session = load_session()
        method_name = '{}_{}'.format(self.http_method, self.url)
        new_model = APIRequestModel(method=method_name,
                                    response_time=self.elapsed)
        session.add(new_model)
        session.commit()
