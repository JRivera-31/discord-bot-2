from weakref import finalize
import discord
import os

from os.path import join, dirname
from pathlib import Path
from dotenv import load_dotenv
from discord.ext import commands

# Grab bot token from .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Set Prefix for commands
client = commands.Bot(command_prefix="pp!", self_bot=False)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# To run the bot
client.run(BOT_TOKEN)