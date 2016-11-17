import discord
import asyncio

# Takes in the command !commands and returns a list of
# the commands thar are available from a file called 'commandlist'
async def commandhelp(client, message):
    command_file = open('commandlist', 'r')
    command_list = []
    for line in command_file:
        command_list.append(line.rstrip())
    await client.send_message(message.channel, ', '.join(command_list))
    command_file.close()

# Takes the !woof command and barks.
async def woof(client, message):
    await client.send_message(message.channel, 'bark')

# Takes the !loveme command and shares the love.
async def loveme(client, message):
    await client.send_message(message.channel, ':heart:')

# Takes the !help command and warns that the sender is distressed.
async def showhelp(client, message):
    sender =  message.author.nick
    await client.send_message(message.channel, 'plz help ' + sender)
    await client.send_message(message.channel, 'they in distress')

# Takes the !git command and returns the URL for the repo.
async def git(client, message):
    url = 'https://github.com/CharlesTalbot123/discord-goopbot'
    await client.send_message(message.channel, url)

# Takes the !bigwoof command and does a big bark.
async def bigwoof(client, message):
    await client.send_message(message.channel, '**BARK**')

# Takes the !woofwoof command and does a couple of barks.
async def woofwoof(client, message):
    await client.send_message(message.channel, 'bark bark')