import discord
from discord.ext import commands
import sys
import subprocess
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
        cmd = [sys.executable] + sys.argv
        subprocess.Popen(cmd)
        await bot.close()
