import subprocess


def start_server():
    return subprocess.call('gunicorn app:api', shell=True)
