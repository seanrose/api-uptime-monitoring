from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table
from sqlalchemy import Integer, String, Float, ForeignKey

engine = create_engine('postgresql://localhost:5432/carnot',
                       echo=True)

metadata = MetaData(bind=engine)

api_test_table = Table(
    'api_tests', metadata,
    Column('id', Integer, primary_key=True),
    Column('http_method', String),
    Column('headers', String),
    Column('uri', String),
    Column('body', String),
    Column('params', String)
)

response_table = Table(
    'responses', metadata,
    Column('id', Integer, primary_key=True),
    Column('api_test_id', None, ForeignKey('api_tests.id')),
    Column('response_time', Float)
)

# create tables in database
metadata.create_all()
