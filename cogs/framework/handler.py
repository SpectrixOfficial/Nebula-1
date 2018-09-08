import discord, asyncio, logging, aiohttp, requests
from discord.ext import commands

class Handler:
    def __init__(self, bot):
        self.bot = bot
    
    async def on_command_error(self, ctx, error):
        if isinstance (error, commands.MissingPermissions):
            if ctx.author.id == 373256462211874836:
                return await ctx.reinvoke()
            else: # This little thing right here saves code, and frustration, if the owner doesnt have permissions, then it will reinvoke the command by bypassing all checks and if else statement the prevent it.
                return await ctx.send(f":x: ***Sorry, But You Have No Permission(s) for The `{ctx.command}` Command***")
        elif isinstance(error, commands.BotMissingPermissions):
            return await ctx.send(f":x: ***Sorry, But I Don't Have No Permission(s) To Run The `{ctx.command}` Command***")
        elif isinstance(error, commands.NoPrivateMessage):
            return await ctx.send(f"Hey, {ctx.command} isn't allowed in DMs, Try It In A Server Please")
        elif isinstance(error, commands.CheckFailure):
            return await ctx.send("***<:tickNo:483288678437879808> These Commands are Only For My Developers***")
        elif isinstance(error, commands.CommandNotFound):
            pass
        else:
            return await ctx.send(f"*** <:tickNo:483288678437879808> {error}***")
        
    async def on_guild_join(self, guild):
        await self.bot.change_presence(activity=discord.Activity(name=f".help in {len(self.bot.guilds)} Servers", url="https://www.twitch.tv/ninja", type=1))
        try:
            await guild.system_channel.send("Hi And Thanks For Inviting Me\nMy Prefix is `.`\nIf You Need Any Help Or Support Please Do `.help` or `.support`")
        except:
            pass
        
    async def on_guild_remove(self):
        await self.bot.change_presence(activity=discord.Activity(name=f".help in {len(self.bot.guilds)} Servers", url="https://www.twitch.tv/ninja", type=1))
            
    async def on_ready(self):
        print("Handler Is Loaded")
        await self.bot.change_presence(activity=discord.Activity(name=f".help in {len(self.bot.guilds)} Servers", url="https://www.twitch.tv/ninja", type=1))
    
    async def on_message(self, message):
        if message.author.bot:
            return

def setup(bot):
    bot.add_cog(Handler(bot))