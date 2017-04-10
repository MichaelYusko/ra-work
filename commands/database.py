import subprocess as sb


def create_db():
    sb.call('alembic upgrade head', shell=True)


def make_migrations():
    sb.call('alembic revision --autogenerate', shell=True)
