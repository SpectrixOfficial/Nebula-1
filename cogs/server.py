import discord, asyncio
from discord.ext import commands

class ServerExclusive:
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx):
        return ctx.guild.id == 490591987477643264

               

def setup(bot):
    bot.add_cog(ServerExclusive(bot))