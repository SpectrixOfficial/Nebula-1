import discord, asyncio, logging, aiohttp, requests, json, time, datetime, math
from discord.ext import commands
from time import ctime

with open("database/data.json") as f:
    config = json.load(f)

class Handler:
    def __init__(self, bot):
        self.bot = bot        
 
    async def on_command_error(self, ctx, error):
        if isinstance (error, commands.MissingPermissions):
            if ctx.author.id != self.bot.owner_id:
                return await ctx.send(f"<:tickNo:490607198443929620> ***Sorry, But You Have Do Not Have The {error.missing_perms[0]} Permission(s)***")
            else:
                await ctx.reinvoke()
        elif isinstance(error, commands.BotMissingPermissions):
            return await ctx.send(f"<:tickNo:490607198443929620> ***Sorry, But I Don't Have No Permission(s) To Run The `{ctx.command}` Command***")
        elif isinstance(error, commands.NoPrivateMessage):
            return await ctx.send(f"***<:tickNo:490607198443929620> Hey, {ctx.command} isn't allowed in DMs, Try It In A Server Please***")
        elif isinstance(error, commands.CheckFailure):
            return await ctx.send("***<:tickNo:490607198443929620> These Commands are Only For My Developers***")
        elif isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.CommandOnCooldown):
            if ctx.author.id != self.bot.owner_id:
                return await ctx.send(f"***<:tickNo:490607198443929620>Woah There, That Command Is On A Cooldown For {math.ceil(error.retry_after)} Seconds***")
            else:
                await ctx.reinvoke()
        else:
            print(f"\nUser Name And ID: {ctx.author} | {ctx.author.id}\nError: {error}")

    async def on_ready(self):
        print("Handler Is Loaded")        
        
    async def on_message(self, msg):
        if msg.author.bot:
            return
        if msg.guild:
            return
        if msg.author.dm_channel:
            print(f"Message Content: {msg.content} | User: {msg.author} | User ID: {msg.author.id}")
    
def setup(bot):
    bot.add_cog(Handler(bot))
