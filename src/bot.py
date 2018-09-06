import discord, asyncio, json, pkg_resources
from discord.ext import commands

with open("data.json") as data:
    config = json.load(data)

def get_prefix():
    return config["bot"]["prefix"]

bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, pm_help=False)
cogs = config["bot"]["cogs"]

if __name__ == '__main__':
    for module in cogs:
        bot.load_extension(module)