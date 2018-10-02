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
            if ctx.author.id != 373256462211874836:
                return await ctx.send(f"<:tickNo:490607198443929620> ***Sorry, But You Have No Permission(s) for The `{ctx.command}` Command***")
            else:
                await ctx.reinvoke()
        elif isinstance(error, commands.BotMissingPermissions):
            return await ctx.send(f"<:tickNo:490607198443929620> ***Sorry, But I Don't Have No Permission(s) To Run The `{ctx.command}` Command***")
        elif isinstance(error, commands.NoPrivateMessage):
            return await ctx.send(f"<:tickNo:490607198443929620> Hey, {ctx.command} isn't allowed in DMs, Try It In A Server Please")
        elif isinstance(error, commands.CheckFailure):
            return await ctx.send("***<:tickNo:490607198443929620> These Commands are Only For My Developers***")
        elif isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.CommandOnCooldown):
            if ctx.author.id != 1373256462211874836:
                return await ctx.send("***<:tickNo:490607198443929620> Command Is On A Cooldown For {} Seconds***".format(math.ceil(error.retry_after)))
            else:
                await ctx.reinvoke()
        else:
            print(f"\nUser Name And ID: {ctx.author}| {ctx.author.id}\nError: {error}")

    async def on_guild_join(self, guild):
        try:
            embed = discord.Embed(color=discord.Color(value=0x1c407a))
            embed.set_author(name="Thanks For Inviting Nebula")
            embed.add_field(name="My Prefix is `.`", value=f"[Support](https://discord.gg/Xgt67WV)")
            embed.add_field(name="Need Help?", value="[Click here](https://enternewname.me/nebula/commands)")
            embed.add_field(name="Logging Channel Requirement", value="***#mod-log***")
            await guild.system_channel.send(embed=embed)
        except:
            pass

    async def on_ready(self):
        print("Handler Is Loaded")
        while True:
            await self.bot.change_presence(activity=discord.Activity(name=f".help in {len(self.bot.guilds)} Servers", url="https://www.twitch.tv/Enter%20New%20Name", type=1))
            await asyncio.sleep(15)
        
    async def on_message(self, msg):
        if msg.author.bot:
            return
        if msg.guild:
            return
        if msg.author.dm_channel:
            print(f"Message Content: {msg.content} | User: {msg.author} | User ID: {msg.author.id}")
    
def setup(bot):
    bot.add_cog(Handler(bot))