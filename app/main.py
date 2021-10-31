from client import BotClient
from config.app import Config


if __name__ == '__main__':
    client = BotClient()
    client.run(Config.BOT_TOKEN)