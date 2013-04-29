from db_session import Base, load_session
from sqlalchemy import Column, Integer, String

session = load_session()


class APITest(Base):
    __tablename__ = 'api_tests'

    id = Column('id', Integer, primary_key=True)
    http_method = Column('http_method', String)
    headers = Column('headers', String)
    uri = Column('uri', String)
    body = Column('body', String)
    params = Column('params', String)

    def __init__(self,
                 http_method,
                 uri,
                 id=None,
                 headers=None,
                 body=None,
                 params=None):

        self.http_method = http_method
        self.uri = uri
        self.id = id
        self.headers = headers or ''
        self.body = body or ''
        self.params = params or ''

    def __repr__(self):

        return '<APITest {} {}>'.format(self.http_method, self.uri)

    def run_test():

        return 'ran test'

    def save_test():

        return

def fetch_api_tests():

    all_api_tests = session.query(
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

    new_api_test = session.add(APITest(http_method,
                                       uri,
                                       headers=None,
                                       body=None,
                                       params=None))

    session.commit()

    return new_api_test
