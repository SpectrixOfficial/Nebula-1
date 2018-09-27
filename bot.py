import discord, asyncio, json, pkg_resources, time, datetime, os, sqlite3
from discord.ext import commands
from time import ctime
from discord.ext.commands import clean_content

with open("database/data.json") as f:
    config = json.load(f)

#The following unselected is still in testing, im too lazy to care right now
"""def get_prefix(msg):
    default_prefix = ["<@487164011683774464>", "."]
    connection = sqlite3.connect('database/data.db')
    db = connection.cursor()
    try:
        db.execute("SELECT * FROM guilddata SELECT ?=? SELECT prefix", msg.guild.id)
        connection.close()
    except:
        return default_prefix
    connection.close()"""
        

bot = commands.Bot(command_prefix=commands.when_mentioned_or(config["prefix"]), case_insensitive=True, clean_content=True, max_messages=300)
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
    await ctx.send(f"I have been running for **{days}** day(s), **{hours}** hour(s), **{minutes}** minute(s), **{seconds}** second(s)!")
    
if __name__ == '__main__':
    for module in cogs:
        print("\nLoading Bot Extension")
        bot.load_extension(module)
    print("\nBot Extensions Are Ready,\nLoading Bot And Connecting Extensions..")
    
bot.run(config["bottoken"], bot=True, reconnect=True)