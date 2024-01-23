import os
from datetime import datetime
import requests
import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix=".", help_command=None, intents=disnake.Intents.all())

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    emoji = "✅"
    await ctx.message.add_reaction(emoji)

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    emoji = "✅"
    await ctx.message.add_reaction(emoji)

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")
    emoji = "✅"
    await ctx.message.add_reaction(emoji)

@bot.command()
@commands.is_owner()
async def off(ctx):
    emoji = "✅"
    await ctx.message.add_reaction(emoji)
    await bot.close()

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
























bot.run("MTE3ODI2NTUxMzk5MDgzMjE1OQ.GkEV0J.k5YBXsX5lg5_mCMyg7TaUHwDFdyXKgv3cH-P_U")