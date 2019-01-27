import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

client = commands.Bot(command_prefix='kiibo')

pistolwhip = discord.Embed()
pistolwhip.set_image(url="https://cdn.discordapp.com/attachments/475075193690390528/498297865068871715/-0.png")

@client.event
async def on_ready():
    print('client KiiboBot ready')
    await client.change_presence(game = discord.Game(
        name = 'Dislikes: Vending Machines'
    ))

@client.command()
async def die():
    await client.say('no u \n https://tinyurl.com/kibdie')
    
@client.command()
async def ahegao():
    await client.say('Uwaaah~~~!!!!! \n https://tinyurl.com/kiibo2')

@client.command()
async def tee():
    await client.say("hee!!")

@client.command()
async def sucks():
    await client.say('no u \n https://tinyurl.com/kiibo1')

@client.command()
async def nukeiran():
    await client.say('Okay, for how long?')

@client.command()
async def playdespacito():
    await client.say('**Aye.** \n https://www.youtube.com/watch?v=kJQP7kiw5Fk')
    
@client.command()
async def imtired():
    await client.say('/Tuck in')
@client.command()
async def imsleepy():
    await client.say('/Tuck in')
@client.command()
async def imgoingtobed():
    await client.say('/Tuck in')
    
@client.command()
async def pats():
    await client.say('https://tinyurl.com/kiibo3')

@client.command()
async def goodnight():
    await client.say('Good night! \nhttps://tinyurl.com/kiibobed')

@client.command()
async def goodmorning():
    await client.say('Good morning! \n https://tinyurl.com/kiibo55')

@client.command()
async def mineforme():
    await client.say('GIVE ME THE GOLD! **WHERE\'S THE GOLD!!!** \n https://tinyurl.com/kiibomine')

@client.command()
async def whosthere():
    await client.say('**MASSIVE LEGEND HERE** \nhttps://tinyurl.com/kiblegend')

@client.command()
async def detect():
    await client.say('Gamer detected.\nhttps://tinyurl.com/kibdetect')

@client.command()
async def rocketpunch():
    await client.say('**WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW**\nhttps://tinyurl.com/kibpunch')
    
@client.command()
async def helpbronte():
    await client.say('not even god can help bronte now')
    
@client.command()
async def riseup():
    await client.say('**RISING UP INITIATED.**')
    
@client.command()
async def hi():
    await client.say('Hello!')

@client.command()
async def representnewbrunswick():
    await client.say('https://tinyurl.com/newbrunsw')

@client.command()
async def suckedmygootuberbehindarbys():
    await client.say('∠( \'ω\')／ Maybe ＼(\'ω\' )>')
    
@client.command()
async def fuckme():
    await client.say('My dick fell off!\nhttps://tinyurl.com/ybgygnkk')

@client.command()
async def chokeme():
    await client.say('https://tinyurl.com/ychvpbdu')
    
@client.command()
async def happyholidays():
    await client.say('Happy holidays! :snowflake:')
   
@client.command()
async def awoo():
    await client.say('<:awoo:518856090746617940>')

@client.command()
async def killthisfool():
    await client.say('Get ready for Kiibo\'s Pistol Whippin\' .45! **SAIONARA!**'),pistolwhip
    
@client.command()
async def sendbirthdaywishes():
    await client.say(':balloon: :balloon: **HAPPY BIRTHDAY** :balloon: :balloon: \nhttps://tinyurl.com/kibbirth')
    
    
@client.command()
async def flex():
    await client.say('i have more money than youll ever see and its all vbucks\nhttps://tinyurl.com/cloutkib')
    
@client.command()
async def sendfunnydogememelol():
    await client.say('https://tinyurl.com/kibohahafunny')
    
@client.command()
async def info():
    await client.say('This bot was made by wren#5626. Commands are subject to frequent change. Do `kiibo help` for a list of options. epic')
    
@client.event
async def on_message(message):
    message.content = message.content.lower().replace(' ', '').replace('\'','').replace('\u2019','')
    await client.process_commands(message)

client.run(os.getenv('TOKEN'))
