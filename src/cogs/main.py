import discord, asyncio, json, time
from time import ctime
from discord.ext import commands

class MainCommands:
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(MainCommands(bot))