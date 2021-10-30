from random import choice

import sys
import random

from discord import Client
from loader import logger


class BotClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    async def on_ready(self):
        logger.success('Starting bot...')


    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.lower() in ['спасибо', 'спс']:
            text = choice(['интересно', 'занятно', 'поше наху'])
            await message.channel.send(text)
        

    async def on_disconnect(self):
        logger.warning('Disconnecting bot...')
    

    async def on_error(self, event: str, *args, **kwargs):
        logger.exception('Event ' + event + ' raised an exception:\n' + str(sys.exc_info()))
        raise