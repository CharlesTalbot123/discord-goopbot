import discord
import asyncio
import random

class Commands:

    isFetch = False

    # Checks to see if the command is within the list and if it is
    # then executes it. !help and !commands both have to be taken
    # care of seperately due to having function names that are
    # different to their command names.
    async def checkcommands(self, client, message):
        in_command = message.content.split(' ')[0].replace('!', '')
        sender = message.author.name
        if in_command == 'help':
            print('Received !help from ' + sender)
            await self.showhelp(client, message)
        elif in_command == 'commands':
            print('Received !commands from ' + sender)
            await self.commandhelp(client, message)
        else:
            if hasattr(self, in_command):
                print('Received !' + in_command + ' from ' + sender)
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
        await client.add_reaction(message, '❤')
        await client.send_message(message.channel, 'arf')

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
        fetchgame = discord.Game()
        fetchgame.name = "fetch!!"
        await client.change_presence(game=fetchgame)
        await client.send_message(message.channel, '*waiting*')

    # Takes in the !throw command and goes to fetch if there's something
    # to fetch. Otherwise, gets confused.
    async def throw(self, client, message):
        if self.isFetch:
            self.isFetch = False
            await client.send_message(message.channel, '***CHASE***')
            await asyncio.sleep(3)
            await client.send_message(message.channel, '*fetched* :tennis:')
            await client.change_presence()
        else:
            await client.send_message(message.channel, '*confused*')

    # Takes the !feed command, and supplies a lovely meal.
    # Puppers might take a variable amount of time to eat.
    async def feed(self, client, message):
        # Dinner is served
        await client.send_message(message.channel, ':dog::meat_on_bone:')
        # Eating
        lim = random.randint(1,5)
        while lim > 0:
            await asyncio.sleep(1)
            await client.send_message(message.channel, '*chomp*')
            lim -= 1
        # Wow
        await client.send_message(message.channel, ':dog::two_hearts:')

    # Takes the !getin [name] command and asks a user with
    # the name [name] to get in.
    async def getin(self, client, message):
        if len(message.content.split(' ')) < 2:
            await client.send_message(message.channel, '*confused*')
            return
        name = message.content.split(' ', 1)[1].lower()
        # If the name matches partially matches the beginning of
        # a user's name in the server, mention them.
        for user in message.server.members:
            if user.nick is not None:
                if user.nick.lower().startswith(name):
                     await client.send_message(message.channel, 'ruff '
                                                + user.mention)
                     return
            if user.name.lower().startswith(name):
                await client.send_message(message.channel, 'ruff '
                                            + user.mention)
                return
        await client.send_message(message.channel, '*confused*')

    async def birthday(self, client, message):
        if len(message.content.split(' ')) < 2:
            await client.send_message(message.channel, '*confused*')
            return
        name = message.content.split(' ', 1)[1]
        await client.send_message(message.channel, 'birthwoof ' + name)
        await client.send_message(message.channel, ':birthday:')

    # Takes in the !echo [echo] command and echos it. But
    # goopbot is a dog, goopbot can't speak.
    async def echo(self, client, message):
        if len(message.content.split(' ')) < 2:
            await client.send_message(message.channel, '*confused*')
            return
        echo = message.content.split(' ', 1)[1].lower().split(' ')
        dog_echo = []
        for word in echo:
            if word.startswith('a'):
                dog_echo.append('arf')
            elif word.startswith('r'):
                dog_echo.append('ruff')
            elif word.startswith('b'):
                dog_echo.append('bark')
            elif word.startswith('f'):
                dog_echo.append('freh')
            elif word.startswith('y'):
                dog_echo.append('yap')
            elif word.startswith('w'):
                dog_echo.append('warf')
            elif word.startswith('z'):
                dog_echo.append('???')
            else:
                dog_echo.append('woof')
        await client.send_message(message.channel, ' '.join(dog_echo))
