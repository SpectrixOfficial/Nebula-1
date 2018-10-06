import discord, asyncio, time
from time import ctime
from discord.ext import commands

class UserManagement:
    def __init__(self, bot):
        self.bot = bot
     
    async def on_ready(self):
        print("User Management Is Loaded")
   
    @commands.command()
    async def ban(self, ctx, user : discord.Member, banReason=None):
        if ctx.author.id == 373256462211874836 or ctx.author == ctx.guild.owner or ctx.author.top_role > user.top_role:
            await ctx.send("hmm")
            

        
# no <:tickNo:483288678437879808> 
#yes <:tickYes:483288647823523841>
def setup(bot):
    bot.add_cog(UserManagement(bot))