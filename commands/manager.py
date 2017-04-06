from commands import DEFAULT_EXECUTE_COMMAND
from commands.database import CREATE_DATABASE


class CommandManager:
    command = None

    def __init__(self, arg):
        self.arg = self.check_command(arg)

    def check_command(self, command):
        try:
            if command == '-c':
                command = CREATE_DATABASE
            if command == 'runserver':
                print('runserver')
            else:
                print(DEFAULT_EXECUTE_COMMAND)
        except IndexError:
            print(DEFAULT_EXECUTE_COMMAND)
        return command
