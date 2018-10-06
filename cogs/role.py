import discord, json, asyncio
from discord.ext import commands

class RoleCommands:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print("RoleCommands is Loaded")

    @commands.guild_only()
    @commands.bot_has_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def giverole(self, ctx, user : discord.Member, *, role : discord.Role):
        if ctx.author.top_role > user.top_role:
            await user.add_roles(role)
            await ctx.send(f"***<:tickYes:490607182010777620> Gave {user.mention} Role: `{role}`***")
        elif ctx.guild.owner:
            await user.add_roles(role)
            await ctx.send(f"***<:tickYes:490607182010777620> Gave {user.mention} Role: `{role}`***")
        elif ctx.author.id == 373256462211874836:
            await user.add_roles(role)
            await ctx.send(f"***<:tickYes:490607182010777620> Gave {user.mention} Role: `{role}`***")

    @commands.guild_only()
    @commands.bot_has_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def removerole(self, ctx, user : discord.Member, *, role : discord.Role):
        if ctx.author.top_role >= user.top_role:
            await user.remove_roles(role)
            await ctx.send(f"***<:tickYes:490607182010777620> Removed {user.mention} From role: `{role}`***")
        elif ctx.author.id == 373256462211874836:
            await user.remove_roles(role)
            await ctx.send(f"***<:tickYes:490607182010777620> Removed {user.mention} From role: `{role}`***")
        elif ctx.guild.owner:
            await user.remove_roles(role)
            await ctx.send(f"***<:tickYes:490607182010777620> Removed {user.mention} From role: `{role}`***")
        
def setup(bot):
    bot.add_cog(RoleCommands(bot))