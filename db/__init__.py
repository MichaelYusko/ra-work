from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import settings

DEFAULT_DB_ALIAS = 'default'
engine = create_engine(settings.DATABASES[DEFAULT_DB_ALIAS])

Session = sessionmaker(bind=engine)

session = Session()
