import sys
from commands import DEFAULT_EXECUTE_COMMAND
from commands.database import create_db
from commands.server import start_server


class CommandManager:
    def __init__(self, arg):
        self.arg = self.check_command(arg)

    def check_command(self, command):
        cmnd = None
        try:
            if command == 'createdb':
                cmnd = create_db()
                sys.exit(1)
            if command == 'runserver':
                cmnd = start_server()
            else:
                print(DEFAULT_EXECUTE_COMMAND)
        except IndexError:
            print(DEFAULT_EXECUTE_COMMAND)
        return cmnd
