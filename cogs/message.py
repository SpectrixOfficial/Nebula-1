import discord, asyncio, logging, time, datetime
from discord.ext import commands

class MessageManagement:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.guild_only()
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    @commands.command(aliases=["purge", "c"])
    async def clear(self, ctx, *, number : int):
        if number > 1000:
            number = 1000
        num = await ctx.channel.purge(limit=number + 1)
        await asyncio.sleep(.7)
        await ctx.send(f"Deleted `{len(num) - 1}` messages <:tickYes:490607198443929620>", delete_after=1)


    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    @commands.command(aliases=['slowmo'])
    async def slowmode(self, ctx, seconds: int=0):
        if seconds == 0:
            await ctx.channel.edit(slowmode_delay=seconds)
            await ctx.send("Slowmode is off for this channel!")
        else:
            if seconds == 1:
                numofmessages = "second"
            else:    
                numofmessages = "seconds"
            await ctx.channel.edit(slowmode_delay=(seconds))
            await ctx.send(f"Channel is On Slowmode for `{seconds}` {numofmessages}!")
    
    
    async def on_ready(self):
        print("MessageManagement Is Loaded")

def setup(bot):
    bot.add_cog(MessageManagement(bot))