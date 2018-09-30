import asyncio, discord, time, random
from discord.ext import commands
from time import strftime

class InfoFetcher:
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(InfoFetcher(bot))