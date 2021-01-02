# liquid-max.p
#
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

import random

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

def maximillian():
    inputFile = open('maximillian.txt','r')
    myList = []

    for line in inputFile:
        myList.append(line.strip())

    msg = random.choice(myList)

    inputFile.close()
    return msg

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-------')

@bot.event
async def on_message(message):
    if (message.content == 'wake up'):
        await message.channel.send(f'Wake up <@792591005525737492>...')

    await bot.process_commands(message)


@bot.command(name='liquid-max')
async def liquid_max(ctx):

    if (ctx.author.id == 792591005525737492):
        msg = maximillian()

    await ctx.send(msg)
    

bot.run(TOKEN)
