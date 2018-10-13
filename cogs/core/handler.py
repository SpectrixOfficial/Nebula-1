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
                return await ctx.send(f"<:tickNo:490607198443929620> ***Sorry, But You Have Do Not Have The `{error.missing_perms[0].replace('_', ' ')}` permission***")
            else:
                try:
                    return await ctx.reinvoke()
                except Exception as err:
                    return await ctx.send(f"```bash\n{err}\n```")
        elif isinstance(error, commands.BotMissingPermissions):
            return await ctx.send(f"<:tickNo:490607198443929620> ***Sorry, But I Don't Have No Permissions To Run The `{ctx.command}` command***")
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
            print(f"\nUser Name And ID: {ctx.author} | {ctx.author.id}\nCommand: {ctx.command}\nError: {error}")        
        
    async def on_message(self, msg):
        if msg.author.bot:
            return
        if msg.guild:
            return
        if msg.author.dm_channel:
            if msg.author.id == self.bot.owner_id:
                return
            else:
                print(f"Message Content:\n{msg.content}\nUser: {msg.author}\nUser ID: {msg.author.id}")
            
def setup(bot):
    bot.add_cog(Handler(bot))
