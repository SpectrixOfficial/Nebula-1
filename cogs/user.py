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
            await user.ban(reason=banReason)
            if not banReason:
                await ctx.send(f"**<:tickYes:490607182010777620> I have banned {user} from the server**")
            else:
                await ctx.send(f"**<:tickYes:490607182010777620> I have banned {user} from the server because: {banReason}**")

    @commands.command()
    async def kick(self, ctx, user : discord.Member, kickReason=None):
        if ctx.author.id == 373256462211874836 or ctx.author == ctx.guild.owner or ctx.author.top_role > user.top_role:
            await user.kick(reason=kickReason)
            if not kickReason:
                await ctx.send(f"**<:tickYes:490607182010777620> I have kicked {user} from the server**")
            else:
                await ctx.send(f"**<:tickYes:490607182010777620> I have kicked {user} from the server because: {kickReason}**")
    
    @commands.command()
    async def softban(self, ctx, user : discord.Member, softbanReason=None):
        if ctx.author.id == 373256462211874836 or ctx.author == ctx.guild.owner or ctx.author.top_role > user.top_role:
            await user.ban(reason=softbanReason)
            await user.unban()
            if not softbanReason:
                await ctx.send(f"**<:tickYes:490607182010777620> I have softbanned {user} from the server**")
            else:
                await ctx.send(f"**<:tickYes:490607182010777620> I have softbanned {user} from the server because: {softbanReason}**")        

        
# no <:tickNo:483288678437879808> 
#yes <:tickYes:483288647823523841>
def setup(bot):
    bot.add_cog(UserManagement(bot))