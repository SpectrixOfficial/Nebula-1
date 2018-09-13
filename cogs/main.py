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
        embed = discord.Embed(color=discord.Color(value=0x1c407a))
        embed.set_author(name="Nebula Bot Commands:")
        embed.add_field(name="List of All Commands:", value="[Click Here For The Site](https://enternewname.me/nebula/commands)")
        await ctx.send(embed=embed)

    @commands.command()
    async def prefix(self, ctx):
        ctx.send("My Prefix is `.` and Cannot Be Changed")

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

    @commands.command()
    async def invite(self, ctx):
        try:
            await ctx.author.send("https://discordapp.com/oauth2/authorize?client_id=487164011683774464&permissions=8&scope=bot")
            await ctx.send("**Check Your DMs For The Nebula Invite!**")
        except:
            await ctx.send("https://discordapp.com/oauth2/authorize?client_id=487164011683774464&permissions=8&scope=bot")

    @commands.guild_only()
    @commands.command()
    async def feedback(self, ctx, *, body : str):
        try:
            feedback = self.bot.get_channel(488912067756294146)
            embed = discord.Embed(color=discord.Color(value=0x1c407a))
            embed.set_author(name="Feedback")
            embed.add_field(name="Guild ID And Name: ", value=f"ID: {ctx.guild.id}, Name: {ctx.guild}", inline=False)
            embed.add_field(name="User", value=f"Name: {ctx.author}, ID: {ctx.author.id}", inline=False)
            embed.add_field(name="Channel ID And Name", value=f"ID: {ctx.channel.id}, Name: #{ctx.channel}", inline=False)
            embed.add_field(name="Response: ", value=body, inline=True)
            await feedback.send(embed=embed)
            await ctx.send("**Your Response Has Been Sent, You Might Recieve A Response Later On**")
        except Exception as e:
            await ctx.send("***Your Feedback Could Not Be Sent <:tickNo:483288678437879808>, Notifying Owner***")
            owner = self.bot.get_user(373256462211874836)
            await owner.send(f"{owner}, We Have A Problem With The Feedback Command,\nAuthor Profile: {ctx.author.id}\nName: {ctx.author}\nHeres The Error:\n```fix\n{e}\n```")

    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    @commands.command(aliases=['a'])
    async def annouce(self, ctx, channel : discord.TextChannel, * ,body : str):
        embed = discord.Embed(color=discord.Color(value=0x1c407a))
        embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author)
        embed.add_field(name="Update:\n", value=body)
        await channel.send(embed=embed)
        try:
            await ctx.message.delete()
        except:
            pass
# no <:tickNo:483288678437879808> 
#yes <:tickYes:483288647823523841>

def setup(bot):
    bot.add_cog(MainCommands(bot))