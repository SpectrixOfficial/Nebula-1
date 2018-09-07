import discord, asyncio, logging, aiohttp, requests
from discord.ext import commands
# No Commands Go Here, Only Background Tasks and Handling Comes
class Handler:
    def __init__(self, bot):
        self.bot = bot
    
    async def on_command_error(self, ctx, error):
        if isinstance (error, commands.MissingPermissions):
            if ctx.author.id == 373256462211874836:
                return await ctx.reinvoke()
            else:
                return await ctx.send(f":x: ***Sorry, But You Have No Permission(s) for {ctx.command} Command***")
        elif isinstance(error, commands.BotMissingPermissions):
            return await ctx.send(f":x: ***Sorry, But I Don't Have No Permission(s) To Run {ctx.command} ***")
        elif isinstance(error, commands.NoPrivateMessage):
            return await ctx.send(f"Hey, {ctx.command} isn't allowed in DMs, Try It In A Server Please")
        elif isinstance(error, commands.CheckFailure):
            return await ctx.send("***:x: These Commands are Only For My Developers***")
        elif isinstance(error, commands.CommandNotFound):
            pass
        else:
            print(f"\n{error}\n")
            return await ctx.send(f"***:x: {error}***")
            
    
    async def on_ready(self):
        print("Handler Is Loaded")
        await self.bot.change_presence(activity=discord.Activity(name=f".help in {len(self.bot.guilds)} Servers", url="https://www.twitch.tv/ninja", type=1))

        


def setup(bot):
    bot.add_cog(Handler(bot))