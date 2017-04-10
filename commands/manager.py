from commands import (CREATE_DATABASE, DEFAULT_EXECUTE_COMMAND, START_SERVER,
                      TEST_CHECK)


class CommandManager:

    COMMANDS = {
        'runserver': START_SERVER,
        'createdb': CREATE_DATABASE,
        'test-check': TEST_CHECK
    }

    def __init__(self, arg):
        self.arg = self.command_process(arg)

    def command_process(self, key):
        return self.COMMANDS.get(key)() \
            if self.COMMANDS.get(key) is not None \
            else print(DEFAULT_EXECUTE_COMMAND)
