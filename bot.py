import discord, asyncio, json, pkg_resources, time, datetime, os, psutil
from discord.ext import commands
from time import ctime
from discord.ext.commands import clean_content

with open("data.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix=commands.when_mentioned_or(config["prefix"]), case_insensitive=True, pm_help=False, clean_content=True)
bot.remove_command('help')
cogs = config["cogs"]
lt = datetime.datetime.utcnow()

@bot.event
async def on_ready():
    print("========================")
    print("Connected To Discord API")
    print("========================\nStats:\n")
    print(f"Discord.py Version : " + pkg_resources.get_distribution("discord.py").version)
    print(f"{bot.user} Is Online At {datetime.datetime.utcnow()}")
    print(f"Guild Count : {len(bot.guilds)}\n")
    
@bot.command()
async def uptime(ctx):
    delta_uptime = datetime.datetime.utcnow() - lt
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"I have been running for **{days}**d, **{hours}**h, **{minutes}**m, **{seconds}**s")
    
if __name__ == '__main__':
    for module in cogs:
        print("\nLoading Bot Extension")
        bot.load_extension(module)
    print("\nBot Extensions Are Ready,\nLoading Bot And Connecting Extensions..")
    
bot.run(config["bottoken"], bot=True, reconnect=True)
