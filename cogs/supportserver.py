import discord, asyncio, datetime
from discord.ext import commands

class SupportExclusive:
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx):
        return ctx.guild.id == 490591987477643264

    @commands.command()
    async def reportbug(self, ctx, *, bug: str=None):
        if not bug:
            try:
                await ctx.author.send("You Need To Specify What the Bug is...\n\nExample:\n`.reportbug the kick command isnt working`")
            except:
                pass
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.red(), title=f"New Bug Report From {ctx.author.name} | ({ctx.author.id})")
        embed.add_field(name="Bug Report Complaint:", value='\n' + bug)
        await self.bot.get_channel(495417184877674499).send(embed=embed)

    @commands.command()
    async def suggest(self, ctx, * , suggestion : str=None):
        if not suggestion:
            try:
                await ctx.author.send("You Need To Specify What To Suggest...\n\nExample:\n`.suggest add a fn cmd`")
            except:
                pass
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.green(), title=f"New Suggestion From {ctx.author.name} | ({ctx.author.id})")
        embed.add_field(name="Suggestion", value='\n' + suggestion)
        await self.bot.get_channel(495417184877674499).send(embed=embed)


def setup(bot):
    bot.add_cog(SupportExclusive(bot))

    