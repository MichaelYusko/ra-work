from db import engine
from models import Base


def create_db():
    try:
        Base.metadata.create_all(engine)
    except Exception as e:
        print('Failed: {}'.format(e))\



CREATE_DATABASE = create_db
