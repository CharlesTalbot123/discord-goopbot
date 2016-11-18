import discord
import asyncio
from commands import *

token_file = open('token', 'r')
token = token_file.read()

client = discord.Client()
commands = Commands()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    await commands.checkcommands(client, message)
    if 'kill' in message.content.lower() and 'goopbot' in message.content.lower():
        # Please don't hurt goopbot. He's a good boy.
        await client.send_message(message.channel, '*frighten*')
    elif 'love' in message.content.lower() and 'goopbot' in message.content.lower():
        await client.send_message(message.channel, '*happy*')

client.run(token)