import requests
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://localhost:5432/carnot', echo=True)
Base = declarative_base(engine)


class APIRequestModel(Base):
    """"""
    __tablename__ = 'responses'
    __table_args__ = {'autoload': True}


def load_session():
    """"""
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


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

    def save_request(self):
        session = load_session()
        method_name = '{}_{}'.format(self.http_method, self.url)
        new_model = APIRequestModel(method=method_name,
                                    response_time=self.elapsed)
        session.add(new_model)
        session.commit()
