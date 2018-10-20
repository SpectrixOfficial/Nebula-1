import discord, asyncio
from discord.ext import commands

class SupportExclusive:
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx):
        return ctx.guild.id == 490591987477643264

    @commands.command()
    async def reportbug(self, ctx, *, bug: str=None):
        if not bug:
            return await ctx.author.send("You Need To Specify What the Bug is...\n\nExample:\n`.reportbug the kick command isnt working`")
        embed = discord.Embed(color=discord.Color.red(), title=f"New Bug Report From {ctx.author.name} | ({ctx.author.id})")
        embed.add_field(name="Complaint", value=bug)


def setup(bot):
    bot.add_cog(SupportExclusive(bot))

    