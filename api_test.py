from db_session import Base, load_session
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api_test_result import save_api_test_result
import requests

session = load_session()


class APITest(Base):
    __tablename__ = 'api_tests'

    id = Column('id', Integer, primary_key=True)
    http_method = Column('http_method', String)
    headers = Column('headers', String)
    uri = Column('uri', String)
    body = Column('body', String)
    params = Column('params', String)

    api_test = relationship("APITestResult", backref='responses')



    def __init__(self,
                 id=None,
                 http_method=None,
                 uri=None,
                 headers=None,
                 body=None,
                 params=None):

        self.id = id
        self.http_method = http_method
        self.uri = uri
        self.headers = headers or ''
        self.body = body or ''
        self.params = params or ''

    def __repr__(self):

        return '<APITest {} {}>'.format(self.http_method, self.uri)

    def run_test(self):

        headers = {'Authorization': 'Bearer hSjjh5cxzvAjRgAIwsjh1rF1nH0hiifz'}
        response = requests.request(self.http_method,
                                    self.uri,
                                    headers=headers)

        if response.status_code == requests.codes.ok:
            print response.json()
            save_api_test_result(self.id,
                                 response.elapsed.total_seconds())

def fetch_api_tests():

    all_api_tests = session.query(
        APITest.id,
        APITest.http_method,
        APITest.uri,
        APITest.headers,
        APITest.body,
        APITest.params
    )

    return all_api_tests


def create_api_test(http_method,
                    uri,
                    headers=None,
                    body=None,
                    params=None):

    new_api_test = APITest(http_method=http_method,
                           uri=uri)

    session.add(new_api_test)
    session.commit()

    return new_api_test
