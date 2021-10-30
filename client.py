import random
import sys

from discord import Client
from pymorphy2 import MorphAnalyzer

from loader import logger


class BotClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.morph = MorphAnalyzer()


    async def on_ready(self):
        logger.success('Starting bot...')


    async def on_message(self, message):
        '''
        С вероятностью 0.1 анализирует сообщение, ищет в нем существительные,
        и, если они есть, то отправляет сообщение "*сущ. в им. п. мн. ч.* для пидоров"
        '''

        if message.author == self.user:
            return
        
        if message.content.lower() in ['спасибо', 'спс']:
            text = random.choice(['интересно', 'занятно', 'поше наху'])
            await message.channel.send(text)

        elif random.randint(1, 100) in range(1, 11):
            nouns = []
            words = [word.strip('.!?,-—') for word in message.content.lower().split()]
            
            for word in words:
                parsed = self.morph.parse(word)[0]
                
                # If the word is a noun
                if 'NOUN' in parsed.tag:
                    inflected = parsed.inflect({'nomn', 'plur'})
                    if inflected:
                        nouns.append(inflected.word)
            
            if nouns:
                await message.channel.send(f'{random.choice(nouns)} для пидоров'.capitalize())


    async def on_disconnect(self):
        logger.warning('Disconnecting bot...')
    

    async def on_error(self, event: str, *args, **kwargs):
        logger.exception('Event ' + event + ' raised an exception:\n' + str(sys.exc_info()))
        raise