import discord, asyncio, json, random, math, os
from discord.ext import commands

class FunCommands:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print("FunCommands Is Loaded")

    @commands.command()
    async def rps(self, ctx):
        await ctx.send(f"**I Choose.... `{random.choice(['Rocks', 'Paper', 'Scissors'])}`**")

    @commands.command(aliases=['ld'])
    async def liedetector(self, ctx, *, input):
        lieresult = random.randint(0, 100)
        if lieresult <= 0 <= 10:
            result = f"Seeing No Lies, {ctx.author.name}"
        elif lieresult <= 11 <= 15:
            result = "I'm Not Smelling Any Lies Yet"
        elif lieresult <= 16 <= 20:
            result = "*Sniff, Sniff*, No Lies, But i am Getting Suspicious"
        elif lieresult <= 21 <= 25:
            result = "I Smell A Lie, Kiddo"         
        elif lieresult <= 26 <= 30:
            result = "***Lie Detector Reports 4 Lies Has Been Told***"
        elif lieresult <= 31 <= 40:
            result = "**WHATS THIS, RUBBISH LIES**"
        elif lieresult <= 41 <= 50:
            result = "LIES LIES LIES"
        elif lieresult <= 51 <= 60:
            result = "***BEEP BEEP BEEP BEEP BEEP :no_entry: ***"
        elif lieresult <= 61 <= 89:
            result = "Damn, you lie so much, even the devil won't accept you"
        elif lieresult <= 90 <= 100:
            result = f"<:Kermit:488902339416293387> WE ALL KNOW YOU ARE LYING!"
        emb = discord.Embed(color=discord.Color(value=0x186391))
        emb.set_author(name="Lie Detector Test")
        emb.add_field(name="Lie Checker", value=input, inline=False)
        emb.add_field(name=f"Result: ", value=result, inline=False)
        emb.add_field(name="Lie Percentage Result: ", value=f"{lieresult}% Percent", inline=False)
        await ctx.send(embed=emb)

    @commands.command()
    async def poll(self, ctx, * ,PollMessage : str):
        embed = discord.Embed(color=discord.Color(value=0x186391))
        embed.set_author(icon_url=ctx.author.avatar_url, name=f"Poll Made By {ctx.author}")
        embed.add_field(name="\uFEFF", value=PollMessage)
        pollmsg = await ctx.send(embed=embed)
        await ctx.message.delete()
        try:
            await pollmsg.add_reaction(emoji=":tickYes:483288647823523841")
            await pollmsg.add_reaction(emoji=":tickNo:483288678437879808")
        except:
            await ctx.send("***Make Sure I have `add_reactions` so I can make the poll***")

    @commands.guild_only()
    @commands.command()
    async def perms(self, ctx, *, user : discord.Member=None):
        if not user:
            user = ctx.author
        permissions = '\n'.join(permission for permission, value in user.guild_permissions if value)
        embed = discord.Embed(title="Total Permissions For Server:", description=ctx.guild.name, color=user.color)
        embed.set_author(icon_url=user.avatar_url, name=str(user))
        embed.add_field(name="\uFEFF", value=permissions)
        await ctx.send(embed=embed, content=None)

def setup(bot):
    bot.add_cog(FunCommands(bot))