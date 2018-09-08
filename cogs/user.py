import discord, asyncio, time
from time import ctime
from discord.ext import commands

class UserManagement:
    def __init__(self, bot):
        self.bot = bot
     
    async def on_ready(self):
        print("User Management Is Loaded")
    
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    @commands.command(aliases=['k'])
    async def kick(self, ctx, user : discord.Member, reason=None):
        if ctx.author.top_role > user.top_role:
            if ctx.author == user:
                return await ctx.send("<:tickNo:483288678437879808> ***You Can't Kick Yourself..***")

            await user.kick(reason=reason)
            await ctx.send(f"**{user} has Been Kicked From The Guild With A Reason:** {reason}")

    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, user : discord.Member, reason=None):
        if ctx.author.top_role > user.top_role:
            if user == ctx.author:
                return await ctx.send("<:tickNo:483288678437879808> ***You Can't Ban Yourself..***")
                
            await user.ban(reason=reason)
            await ctx.send(f"<:tickYes:483288647823523841> **{user} has Been Banned From The Guild With A Reason:** {reason}") 

    @commands.has_permissions(ban_members=True)
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @commands.command()
    async def softban(self, ctx, user : discord.Member, reason=None):
        if ctx.author.top_role > user.top_role:
            if user == ctx.author:
                return await ctx.send("<:tickNo:483288678437879808> ***You Can't Softban Yourself..***")
            await user.ban(reason=reason, delete_message_days=7)
            await user.unban(reason=f"{ctx.author} Softbanned This User | {ctx.author.id}")
            await ctx.send(f"<:tickYes:483288647823523841> **{user} has Been Softbanned From The Guild With A Reason:** {reason}")
        
# no <:tickNo:483288678437879808> 
#yes <:tickYes:483288647823523841>
def setup(bot):
    bot.add_cog(UserManagement(bot))