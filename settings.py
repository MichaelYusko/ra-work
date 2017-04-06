import os

from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '.env')
a = load_dotenv(env_path)

DATABASE = os.environ.get('DATABASE')
