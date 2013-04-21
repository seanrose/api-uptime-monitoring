from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table
from sqlalchemy import Integer, String, Float

engine = create_engine('postgresql://localhost:5432/carnot',
                       echo=True)

metadata = MetaData(bind=engine)

responses_table = Table(
    'responses', metadata,
    Column('id', Integer, primary_key=True),
    Column('method', String(100)),
    Column('response_time', Float)
)

# create tables in database
metadata.create_all()
