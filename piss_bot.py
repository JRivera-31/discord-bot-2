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

client = commands.Bot(command_prefix="pp!")