from db_session import Base, load_session
from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship, backref

session = load_session()


class APITestResult(Base):
    __tablename__ = 'responses'

    id = Column('id', Integer, primary_key=True)
    api_test_id = Column('api_test_id', None, ForeignKey('api_tests.id'))
    response_time = Column('response_time', Float)

    api_test = relationship("APITest", backref=backref('api_tests'))

    def __init__(self,
                 api_test_id=None,
                 response_time=None,
                 id=None):

        self.api_test_id = api_test_id
        self.id = id
        self.response_time = response_time


def save_api_test_result(api_test_id,
                         response_time):

    new_api_test_result = APITestResult(response_time=response_time,
                                        api_test_id=api_test_id)

    session.add(new_api_test_result)
    session.commit()

    return new_api_test_result
