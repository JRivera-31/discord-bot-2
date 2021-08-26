import discord
from discord import channel
from discord import user
from discord import reaction
from discord.ext import commands
from discord.ext.commands.core import command

class ForRoles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def on_ready(self):
        ChID = ''
        if reaction.message.channel.id != ChID:
            return
        if reaction.emoji == '':
            roleName = discord.utils.get(user.server.roles, name='')
            await command.add_roles(user, roleName)

def setup(client):
    client.add_cog(ForRoles(client))