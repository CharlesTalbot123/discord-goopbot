import discord
import asyncio
import random

class Reacts:

    # Checks the message against the variety of reactions that
    # goopbot can do.
    async def checkreacts(self, client, message):
        content = message.content
        if 'kill' in content.lower() and 'goopbot' in content.lower():
            await self.goopbothate(client, message)
        elif 'love' in content.lower() and 'goopbot' in content.lower():
            await self.goopbotlove(client, message)
        elif 'good' in content.lower() and 'boy' in content.lower():
            await self.goodboy(client, message)

    # Reacts to 'love' and 'goopbot' being in the same sentence.
    async def goopbotlove(self, client, message):
        await client.send_message(message.channel, '*happy*')

    # Reacts to 'kill' and 'goopbot' being in the
    # same sentence.
    async def goopbothate(self, client, message):
        await client.send_message(message.channel, '*frighten*')

    # Reacts to 'good' and 'boy' being in the same sentence.
    # goopbot good boy.
    async def goodboy(self, client, message):
        await client.send_message(message.channel, '*happy boy*')
