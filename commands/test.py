import subprocess as sb


def test_check():
    return sb.call(
        'flake8 . --max-line-length=100 --exclude=migrations/versions,bin',
        shell=True
    )
