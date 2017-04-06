from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from settings import DATABASE

engine = create_engine(DATABASE)

Session = sessionmaker(bind=engine)

session = Session()
