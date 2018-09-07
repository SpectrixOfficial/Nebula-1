import discord, asyncio, time
from time import ctime
from discord.ext import commands

class UserManagement:
    def __init__(self, bot):
        self.bot = bot
     
    async def on_ready(self):
        print("User Management Is Loaded")
    
    @commands.has_permissions(kick_members=True)
    @commands.bot.has_permissions(kick_members=True)
    @commands.command(aliases=['k'])
    async def kick(self, ctx, user : discord.Member, reason=None):
        await user.kick(reason=reason)
        await ctx.send(f"**{user} has Been Kicked From The Guild With A Reason:** {reason}") 

    @commands.has_permissions(ban_members=True)
    @commands.bot.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, user : discord.Member, reason=None):
        await user.ban(reason=reason)
        await ctx.send(f"**{user} has Been Banned From The Guild With A Reason:** {reason}") 

def setup(bot):
    bot.add_cog(UserManagement(bot))