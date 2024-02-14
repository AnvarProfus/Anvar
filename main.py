import asyncio
import os
import random
import signal
import discord
from discord.ext import commands
import sys
import subprocess

import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)
SEC=0x2b2d31
@bot.event
async def on_ready():
    print('Бот запущен!')
    channel = bot.get_channel(1182019428402086020)
    await channel.send("Бот запущен! <@644585864864858193>") 

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def calc(ctx, a: int, oper: str, b: int):
    if oper == "+":
        result = a + b
    elif oper == "-":
        result = a - b
    elif oper == "*":
        result = a * b
    elif oper == "/":
        if b != 0:
            result = a / b
        else:
            await ctx.send("Деление на ноль невозможно!")
            return
    else:
        result = "Неверный оператор. Все операторы: \nПлюс - `+` \nМинус - `-` \nУмножить - `*` \nРазделить - `/`"
    await ctx.send(str(result))

@bot.command()
async def say(ctx, *, message):
    embed = discord.Embed(
    description=message, 
    color = SEC
    )
    await ctx.send(embed=embed)



@bot.command()
async def restart(ctx):
    await ctx.send('Бот перезапускается...')
    pid = os.getpid()
    python_executable = sys.executable
    cmd = [python_executable] + sys.argv

    # Ваш код для перезапуска бота
    subprocess.Popen(cmd)
    await bot.close()

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command()
async def mem(ctx):
    image_files = ['images/mem1.jpg', 'images/mem2.jpg', 'images/mem3.jpg']
    random_image = random.choice(image_files)
    with open(random_image, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
