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
    elif message.content.startswith('!loveme'):
        print('Received !loveme from ' + message.author.nick)
        await loveme(client, message)
    elif message.content.startswith('!help'):
        print('Received !help from ' + message.author.nick)
        await showhelp(client, message)
    elif message.content.startswith('!git'):
        print('Received !git from ' + message.author.nick)
        await git(client, message)
    elif message.content.startswith('!bigwoof'):
        print('Reveived !bigwoof from ' + message.author.nick)
        await bigwoof(client, message)
    elif message.content.startswith('!woofwoof'):
        print('Reveived !woofwoof from ' + message.author.nick)
        await woofwoof(client, message)
    elif message.content.startswith('!woof'):
        print('Received !woof from ' + message.author.nick)
        await woof(client, message)

client.run(token)