import discord, asyncio, json, pkg_resources, time, datetime, os
from discord.ext import commands
from time import ctime

with open("data.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix=commands.when_mentioned_or(config["bot"]["prefix"]), case_insensitive=True, pm_help=False, clean_content=False)
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
    print("Bot Version : 0.0.2\n")
    
if __name__ == '__main__':
    for module in cogs:
        print("\nLoading Bot Extension")
        bot.load_extension(module)
    print("\nBot Extensions Are Loaded")
    
bot.run(config["bot"]["discordapitoken"], bot=True, reconnect=True)