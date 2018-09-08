import discord, json, asyncio
from discord.ext import commands

class RoleCommands:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print("RoleCommands is Loaded")

    @commands.command()
    async def giverole(self, ctx, user : discord.Member,* , role : discord.Role):
       if ctx.author.top_role > user.top_role:
            if ctx.author == user:
                if ctx.author.top_role < role.top_role:
                    return await ctx.send("<:tickNo:483288678437879808> ***You can't give Yourself Roles")
                else: 
                    pass
            await user.add_roles(role)

def setup(bot):
    bot.add_cog(RoleCommands(bot))