from client import BotClient
from loader import BOT_TOKEN


if __name__ == '__main__':
    client = BotClient()
    client.run(BOT_TOKEN)