from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://localhost:5432/carnot', echo=True)
Base = declarative_base(engine)
metadata = MetaData(bind=engine)


def load_session():
    """"""
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
