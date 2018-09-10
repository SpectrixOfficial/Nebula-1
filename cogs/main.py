import discord, asyncio, json, time, datetime
from time import ctime
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class MainCommands:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print("MainCommands Is Loaded")

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(color=discord.Color(value=0x877c1f))
        embed.set_author(name="Commands Currently Available")
        embed.add_field(name="Redeveloping Commands", value="[Click Here For The Site](https://enternewname.github.io/home)")
        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command()
    async def perms(self, ctx, *, user : discord.Member=None):
        if not user:
            user = ctx.author
        permissions = ', '.join(permission for permission, value in user.guild_permissions if value)
        embed = discord.Embed(title="Total Permissions For Server:", description=ctx.guild.name, color=user.color)
        embed.set_author(icon_url=user.avatar_url, name=str(user))
        embed.add_field(name="\uFEFF", value=permissions)
        await ctx.send(embed=embed, content=None)

    @commands.cooldown(1, 20, BucketType.channel)
    @commands.command()
    async def ping(self, ctx):
        pong = time.perf_counter()
        msg = await ctx.send("Pinging..")
        pong2 = time.perf_counter()
        pingbinding = pong2 - pong
        result = (round(pingbinding * 1000))
        await msg.edit(content=f":ping_pong:Pong, My Ping Was {result}ms, My Latency is {round(self.bot.latency * 1000)}ms")

    @commands.guild_only()
    @commands.command(aliases=['server'])
    async def support(self, ctx):
        try:
            await ctx.author.send("Here Is The Official Support Server\nhttps://discord.gg/tpHG7NC")
            await ctx.send("***Check DMs For Support Server <:tickYes:483288647823523841>***")
        except:
            await ctx.send("Here Is The Official Support Server\nhttps://discord.gg/tpHG7NC")


def setup(bot):
    bot.add_cog(MainCommands(bot))