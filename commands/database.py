import subprocess as sb


def create_db():
    sb.call('alembic upgrade head', shell=True)
