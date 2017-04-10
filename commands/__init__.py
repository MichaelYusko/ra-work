from .server import start_server
from .database import create_db
from .test import test_check


############################################
# Text for the terminal, with valid commands.
############################################
GREEN_COLOR = '\33[32m'
GREEN_END = '\033[0m'
DEFAULT_EXECUTE_COMMAND = 'Valid commands\n' + GREEN_COLOR + '\tcreatedb ' \
    + GREEN_END + 'create database\n' \
    + GREEN_COLOR + '\trunserver ' \
    + GREEN_END + 'run local server'


###################################
# Constants for ManageCommand class
###################################
CREATE_DATABASE = create_db
START_SERVER = start_server
TEST_CHECK = test_check
