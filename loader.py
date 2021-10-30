import os

from dotenv import load_dotenv
from loguru import logger


env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    load_dotenv(env_path)

# Discord client
BOT_TOKEN = os.getenv('BOT_TOKEN')