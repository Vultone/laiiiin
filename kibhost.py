import discord
from discord.ext import commands

client = commands.Bot(command_prefix='kiibo')

@client.event
async def on_ready():
    print('client KiiboBot ready')
    await client.change_presence(game = discord.Game(
        name = 'If you see this message, I work!'
    ))

@client.command()
async def hi():
    await client.say('Hello! I\'m being hosted somewhere else right now!')

@client.event
async def on_message(message):
    message.content = message.content.lower().replace(' ', '').replace('\'','').replace('\u2019','')
    await client.process_commands(message)

client.run(os.getenv('TOKEN'))
