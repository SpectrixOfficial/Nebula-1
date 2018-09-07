import discord, asyncio, time
from time import ctime
from discord.ext import commands

class UserManagement:
    def __init__(self, bot):
        self.bot = bot
     
    async def on_ready(self):
        print("User Management Is Loaded")


def setup(bot):
    bot.add_cog(UserManagement(bot))