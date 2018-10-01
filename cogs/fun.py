import discord, asyncio, json, random, math, os, aiohttp
from discord.ext import commands
from discord.ext.commands import clean_content


class FunCommands:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print("FunCommands Is Loaded")

    @commands.command()
    async def rps(self, ctx, choice):
        botChoice = random.choice(['rock', 'paper', 'scissors'])

        async def userWins():
            await ctx.send(f"I choose... **{botChoice}**. You win! ***{choice} beats {botChoice}!***")

        async def botWins():
            await ctx.send(f"I choose... **{botChoice}**. I win! ***{botChoice} beats {choice}!***")

        if choice == botChoice:
            await ctx.send(f"***Tie!*** We both used {botChoice}!")

        elif choice == "rock":
            if botChoice == "paper":
                await botWins()
            else:
                await userWins()
        elif choice == "paper":
            if botChoice == "scissors":
                await botWins()
            else:
                await userWins()    
        elif choice == "scissors":
            if botChoice == "paper":
                await botWins()
            else:
                await userWins()


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
            result = f"<:Kermit:490607143771439116> WE ALL KNOW YOU ARE LYING!"
        emb = discord.Embed(color=discord.Color(value=0x1c407a))
        emb.set_author(name="Lie Detector Test")
        emb.add_field(name="Lie Checker", value=input, inline=False)
        emb.add_field(name=f"Result: ", value=result, inline=False)
        emb.add_field(name="Lie Percentage Result: ", value=f"{lieresult}% Percent", inline=False)
        await ctx.send(embed=emb)

    @commands.command()
    async def poll(self, ctx, * ,PollMessage : clean_content):
        embed = discord.Embed(color=discord.Color(value=0x1c407a))
        embed.set_author(icon_url=ctx.author.avatar_url, name=f"Poll Made By {ctx.author}")
        embed.add_field(name="\uFEFF", value=PollMessage)
        pollmsg = await ctx.send(embed=embed)
        await ctx.message.delete()
        try:
            await pollmsg.add_reaction(emoji=":tickYes:490607182010777620")
            await pollmsg.add_reaction(emoji=":tickNo:490607198443929620")
        except:
            await ctx.send("***Make Sure I have `add_reactions` so I can make the poll***")

    @commands.guild_only()
    @commands.command()
    async def perms(self, ctx, *, user : discord.Member=None):
        if not user:
            user = ctx.author
        permissions = '\n'.join(permission for permission, value in user.guild_permissions if value)
        embed = discord.Embed(color=user.color)
        embed.set_author(name=str(user))
        embed.add_field(name="\uFEFF", value=permissions)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(icon_url=ctx.guild.icon_url, text=ctx.guild)
        await ctx.send(embed=embed, content=None)
   
def setup(bot):
    bot.add_cog(FunCommands(bot))