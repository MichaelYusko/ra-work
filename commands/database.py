from db import engine
from models import Base


def create_db():
    try:
        print('Database created')
        return Base.metadata.create_all(engine)
    except Exception as e:
        print('Failed: {}'.format(e))
