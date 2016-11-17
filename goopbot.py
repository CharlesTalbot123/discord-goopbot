import discord
import asyncio
from commands import *

token_file = open('token', 'r')
token = token_file.read()

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!commands'):
        print('Received !commands from ' + message.author.nick)
        await commandhelp(client, message)
    elif message.content.startswith('!woof'):
        print('Received !woof from ' + message.author.nick)
        await woof(client, message)
    elif message.content.startswith('!loveme'):
        print('Received !loveme from ' + message.author.nick)
        await loveme(client, message)
    elif message.content.startswith('!help'):
        print('Received !help from ' + message.author.nick)
        await showhelp(client, message)
    elif message.content.startswith('!testemoji'):
        for emoji in client.get_all_emojis():
            print(emoji.name)

client.run(token)