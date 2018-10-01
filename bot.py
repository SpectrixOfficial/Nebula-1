import discord, asyncio, json, pkg_resources, time, datetime, logging
from discord.ext import commands
from time import ctime

with open("database/data.json") as f:
    config = json.load(f)

bot = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or(config["prefix"]), 
                             case_insensitive=True,
                             clean_content=True,
                             max_messages=300,
                             owner_id=373256462211874836)

bot.remove_command('help')
cogs = config["cogs"]
lt = datetime.datetime.utcnow()

@bot.event
async def on_ready():
    print("========================\nConnected To Discord API")
    print("========================\nStats:\n")
    print("Discord.py Version : " + pkg_resources.get_distribution("discord.py").version)
    print(f"{bot.user} Is Online At {datetime.datetime.utcnow()}")
    print(f"Guild Count : {len(bot.guilds)}\n")
        
@bot.command()
async def uptime(ctx):
    delta_uptime = datetime.datetime.utcnow() - lt
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"I have been running for **{days}** day(s), **{hours}** hour(s),\
                    **{minutes}** minute(s), **{seconds}** second(s)!")

if __name__ == '__main__':
    for module in cogs:
        bot.load_extension(module)
        print(f"\nLoading Extension {module}")
    print("\nConnecting To The API")
    
    bot.run(config["bottoken"], bot=True, reconnect=True)