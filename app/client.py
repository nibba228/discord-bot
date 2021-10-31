import random
import sys

from discord import Client
from pymorphy2 import MorphAnalyzer

from config.app import logger


class BotClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.morph = MorphAnalyzer()

    async def on_ready(self):
        logger.success('Starting bot...')

    async def on_message(self, message):
        '''
        С каким-то шансом анализирует сообщение, ищет в нем существительные,
        и, если они есть, то отправляет сообщение "*сущ. в им. п. мн. ч.* для пидоров"
        '''

        if message.author == self.user:
            return
        
        if message.content.lower() in ['спасибо', 'спс']:
            text = random.choice(['интересно', 'занятно', 'поше наху'])
            await message.channel.send(text)

        elif self._is_appeal(message):
            await message.channel.send(random.choice(['Извините', 'Простите']))

        elif int(random.random()) * 1000 == 397: # random float
            nouns = self._find_nouns(message)
            if nouns:
                await message.channel.send(f'{random.choice(nouns)} для пидоров'.capitalize())


    async def on_disconnect(self):
        logger.warning('Disconnecting bot...')
    
    async def on_error(self, event: str, *args, **kwargs):
        logger.exception('Event ' + event + ' raised an exception:\n' + str(sys.exc_info()))
        raise

    def _is_appeal(self, message):
        appeal = set([w.strip('.,') for w in message.content.lower().split()])
        return {'извинись', 'бот'} <= appeal or {'извиняйся', 'бот'} <= appeal

    def _find_nouns(self, message):
        nouns = []
        words = [word.strip('.!?,-—') for word in message.content.lower().split()]
            
        for word in words:
            parsed = self.morph.parse(word)[0]
            
            # is noun but is not a name, surname or patronymic
            if len(parsed.word) > 3 and 'NOUN' in parsed.tag \
               and 'Name' not in parsed.tag and 'Surn' not in parsed.tag \
               and 'Patr' not in parsed.tag:
                inflected = parsed.inflect({'nomn', 'plur'})
                if inflected:
                    nouns.append(inflected.word)
        return nouns