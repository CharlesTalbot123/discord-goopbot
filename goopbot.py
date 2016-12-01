import discord
import asyncio
from commands import *
from reacts import *

token_file = open('token', 'r')
token = token_file.read()

client = discord.Client()
commands = Commands()
reacts = Reacts()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!'):
        await commands.checkcommands(client, message)
    await reacts.checkreacts(client, message)

client.run(token)