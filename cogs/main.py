import discord, asyncio, json, time
from time import ctime
from discord.ext import commands

class MainCommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True) 
    async def help(self, ctx):
        embed = discord.Embed(color=discord.Color(value=0x877c1f))
        embed.set_author(name="Commands Currently Available")
        embed.add_field(name="Developing New Ones", value="There Is None ATM")
        await ctx.send(embed=embed)

    @commands.command()
    async def perms(self, ctx, *, user : discord.Member=None):
        if not user:
            user = ctx.author
        permissions = '\n'.join(permission for permission, value in user.guild_permissions if value)
        embed = discord.Embed(title="Total Permissions For:", description=ctx.guild.name, color=user.color)
        embed.set_author(icon_url=user.avater_url, name=str(user))
        embed.add_field(name="\uFEFF", value=permissions)
        await ctx.send(embed=embed, content=None)

def setup(bot):
    bot.add_cog(MainCommands(bot))