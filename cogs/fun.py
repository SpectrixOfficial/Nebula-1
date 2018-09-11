import discord, asyncio, json, random, math, os
from discord.ext import commands

class FunCommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rps(self, ctx):
        await ctx.send(f"**I Choose.... `{random.choice(['Rocks', 'Paper', 'Scissors'])}`**")

    
    @commands.command()
    async def liedetector(self, ctx, input):
        lieresult = random.randint(0, 100)
        if lieresult <= 0 <= 10:
            result = "My Lie Detector Is Detecting that He Is Telling The Truth"
        elif lieresult <= 11 <= 15:
            result = f"Detecting The Truth, Not Smelling Any Lies... *yet*"
        elif lieresult <= 20 <= 30:
            result = ":octagonal_sign:  Hol Up, I Sniff A Lie"
        elif lieresult <= 40 <= 50:
            result = "*I smell nothing but liesss*"
        elif lieresult <= 60 <= 70:
            result = "***BEEP BEEP BEEP BEEP BEEP***"
        elif lieresult <= 80 <= 100:
            result = f"<:Kermit:488902339416293387> Nigga You Lying {lieresult}%"
        else:
            result = "You Broke the Lie Detector, :cry:"
        emb = discord.Embed(color=discord.Color(value=0x186391))
        emb.set_author(name="Lie Detector Test")
        emb.add_field(name=f"Result: ", value=result, inline=False)
        emb.add_field(name="Lie Percentage Result: ", value=f"{lieresult}% Percent", inline=False)
        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(FunCommands(bot))