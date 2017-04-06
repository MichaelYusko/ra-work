from commands import DEFAULT_EXECUTE_COMMAND
from commands.database import create_db


class CommandManager:
    def __init__(self, arg):
        self.arg = self.check_command(arg)

    def check_command(self, command):
        cmnd = None
        try:
            if command == 'createdb':
                cmnd = create_db()
            if command == 'runserver':
                cmnd = ''
                print('runserver')
            else:
                print(DEFAULT_EXECUTE_COMMAND)
        except IndexError:
            print(DEFAULT_EXECUTE_COMMAND)
        return cmnd
