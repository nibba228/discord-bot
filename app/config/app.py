import os

from loguru import logger
from dotenv import load_dotenv

from config._logger import LoggerConfig


env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    load_dotenv(env_path)


class Config:
    BOT_TOKEN = os.getenv('BOT_TOKEN')


logger.configure(**LoggerConfig.config_handlers)    