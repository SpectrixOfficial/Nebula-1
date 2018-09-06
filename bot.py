import discord, asyncio, json, pkg_resources, time, datetime
from discord.ext import commands
from time import ctime

with open("data.json") as f:
    config = json.load(f)

def get_prefix(bot, command):
    return commands.when_mentioned_or(config["bot"]["prefix"])

bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, pm_help=False)
bot.remove_command('help')
cogs = config["bot"]["cogs"]

@bot.event
async def on_ready():
    print("========================")
    print("Connected To Discord API")
    print("========================\nStats:\n")
    print(f"Discord.py Version : " + pkg_resources.get_distribution("discord.py").version)
    print(f"{bot.user} Is Online At {datetime.datetime.utcnow()}")
    print(f"Guild Count : {len(bot.guilds)}\n")
    print("Bot Version : 0.0.1\n")
    
if __name__ == '__main__':
    for module in cogs:
        bot.load_extension(module)
    print("\nAll Extensions Loaded")
    
bot.run(config["bot"]["discordapitoken"], bot=True, reconnect=False)