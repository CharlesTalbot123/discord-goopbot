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
        print('Received !commands from ' + message.author.name)
        await commandhelp(client, message)
    elif message.content.startswith('!loveme'):
        print('Received !loveme from ' + message.author.name)
        await loveme(client, message)
    elif message.content.startswith('!help'):
        print('Received !help from ' + message.author.name)
        await showhelp(client, message)
    elif message.content.startswith('!git'):
        print('Received !git from ' + message.author.name)
        await git(client, message)
    elif message.content.startswith('!bigwoof'):
        print('Reveived !bigwoof from ' + message.author.name)
        await bigwoof(client, message)
    elif message.content.startswith('!woofwoof'):
        print('Reveived !woofwoof from ' + message.author.name)
        await woofwoof(client, message)
    elif message.content.startswith('!woof'):
        print('Received !woof from ' + message.author.name)
        await woof(client, message)
    elif message.content.startswith('!hug'):
        print('Received !hug from ' + message.author.name)
        await hug(client, message)
    elif 'kill' in message.content.lower() and 'goopbot' in message.content.lower():
        # Please don't hurt goopbot. He's a good boy.
        await client.send_message(message.channel, '*frighten*')
    elif 'love' in message.content.lower() and 'goopbot' in message.content.lower():
        await client.send_message(message.channel, '*happy*')

client.run(token)