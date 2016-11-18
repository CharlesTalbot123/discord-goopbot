import discord
import asyncio

class Commands:

    isFetch = False

    # Checks to see if the command is within the list and if it is
    # then executes it. !help and !commands both have to be taken
    # care of seperately due to having function names that are
    # different to their command names.
    async def checkcommands(self, client, message):
        in_command = message.content.split(' ')[0].replace('!', '')
        if in_command == 'help':
            await self.showhelp(client, message)
        elif in_command == 'commands':
            await self.commandhelp(client, message)
        else:
            if hasattr(self, in_command):
                cmd = getattr(self, in_command)
                await cmd(client, message)

    # Takes in the command !commands and returns a list of
    # the commands thar are available from a file called 'commandlist'
    async def commandhelp(self, client, message):
        command_list = self.get_commands()
        await client.send_message(message.channel, ', '.join(command_list))

    # Gets the list of commands within the 'commandlist' file.
    def get_commands(self):
        command_file = open('commandlist', 'r')
        command_list = []
        for line in command_file:
            command_list.append(line.rstrip())
        command_file.close()
        return command_list

    # Takes the !woof command and barks.
    async def woof(self, client, message):
        await client.send_message(message.channel, 'bark')

    # Takes the !loveme command and shares the love.
    async def loveme(self, client, message):
        await client.send_message(message.channel, ':heart:')

    # Takes the !help command and warns that the sender is distressed.
    async def showhelp(self, client, message):
        sender =  message.author.nick
        if sender is None:
            sender = message.author.name
        await client.send_message(message.channel, 'plz help ' + sender)
        await client.send_message(message.channel, 'they in distress')

    # Takes the !git command and returns the URL for the repo.
    async def git(self, client, message):
        url = 'https://github.com/CharlesTalbot123/discord-goopbot'
        await client.send_message(message.channel, url)

    # Takes the !bigwoof command and does a big bark.
    async def bigwoof(self, client, message):
        await client.send_message(message.channel, '**BARK**')

    # Takes the !woofwoof command and does a couple of barks.
    async def woofwoof(self, client, message):
        await client.send_message(message.channel, 'bark bark')

    # Takes the !hug command and gives the sender a well needed hug.
    async def hug(self, client, message):
        sender = message.author.nick
        if sender is None:
            sender = message.author.name
        await client.send_message(message.channel, '*doghugs for ' + sender + '*')

    # Takes the !smile command and shows their affection.
    async def smile(self, client, message):
        await client.send_message(message.channel, ':dog:')

    # Takes in the !fetch command and initiates a game of fetch.
    async def fetch(self, client, message):
        self.isFetch = True
        await client.send_message(message.channel, '*waiting*')

    # Takes in the !throw command and goes to fetch if there's something
    # to fetch. Otherwise, gets confused.
    async def throw(self, client, message):
        if self.isFetch:
            self.isFetch = False
            await client.send_message(message.channel, '***CHASE***')
            await asyncio.sleep(3)
            await client.send_message(message.channel, '*fetched* :tennis:')
        else:
            await client.send_message(message.channel, '*confused*')