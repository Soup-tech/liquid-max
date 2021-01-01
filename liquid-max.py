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

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-------')

@bot.event
async def on_message(message):
    print('wake up')
    if (message.content == 'wake up'):
        await message.channel.send(f'Wake up <@792591005525737492>...')
    
    if (message.content == f'<@793190489788645466>'):
        await message.channel.send('control is an illusion')

bot.run(TOKEN)
