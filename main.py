from random import choice
from loader import client, BOT_TOKEN, logger


@client.event
async def on_ready():
    logger.success('Starting bot...')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower() == 'спасибо':
        text = choice(['интересно', 'занятно', 'поше наху'])
        await message.channel.send(text)


if __name__ == '__main__':
    client.run(BOT_TOKEN)