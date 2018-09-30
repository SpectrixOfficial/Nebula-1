import discord, asyncio
from discord.ext import commands

class ServerExclusive:
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx):
        return ctx.guild.id == 490591987477643264

    @commands.command()
    async def test(self, ctx):
        await ctx.send("ing")

     #called an exclusive for a reason you know
               

def setup(bot):
    bot.add_cog(ServerExclusive(bot))