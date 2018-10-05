import discord, asyncio, json, pkg_resources, time, datetime, aiohttp, logging, aiosqlite
from discord.ext import commands
from time import ctime

with open("database/data.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix=commands.when_mentioned_or(config['defaultprefix']), case_insensitive=True, clean_content=True)
bot.remove_command('help')
cogs = config["cogs"]
lt = datetime.datetime.utcnow()
header = {"Authorization" : config["dbltoken"]}
payload = {"server_count"  : len(bot.guilds)}
logging.basicConfig(level=logging.INFO)

async def presencehandler():
    await bot.change_presence(activity=discord.Activity(name=f".help in {len(bot.guilds)} Servers", url="https://www.twitch.tv/EnterNewName", type=1))
    async with aiohttp.ClientSession() as session:
        await session.post("https://discordbots.org/bot/487164011683774464/stats",  data=payload, headers=header)

@bot.event
async def on_guild_remove(guild):
    try:
        await presencehandler()
    except Exception as e:
        await presencehandler()
        print(f"Having A Problem With Loading The presence_handler\nHeres The Error: {e}")  

@bot.event
async def on_ready():
    await presencehandler()
    print("========================\nConnected To Discord API")
    print("========================\nStats:\n")
    print("Discord.py Version : " + pkg_resources.get_distribution("discord.py").version)
    print(f"{bot.user} Is Online At {datetime.datetime.utcnow()}")
    print(f"Guild Count : {len(bot.guilds)}\n")

@bot.event
async def on_guild_join(guild):
    try:
        await presencehandler()
    except Exception as e:
        await presencehandler()
        print(f"Having A Problem With Loading The presence_handler\nHeres The Error: {e}")            
    try:
        embed = discord.Embed(color=discord.Color(value=0x1c407a))
        embed.set_author(name="Thanks For Inviting Nebula")
        embed.add_field(name="My Prefix is `.`", value=f"[Support](https://discord.gg/Xgt67WV)")
        embed.add_field(name="Need Help?", value="[Click here](https://enternewname.me/nebula/commands)")
        embed.add_field(name="Logging Channel Requirement", value="***#mod-log***")
        await guild.system_channel.send(embed=embed)
    except:
        pass
        
@bot.command()
async def uptime(ctx):
    delta_uptime = datetime.datetime.utcnow() - lt
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"I have been running for **{days}** day(s), **{hours}** hour(s), **{minutes}** minute(s), **{seconds}** second(s)!")

if __name__ == '__main__':
    for module in cogs:
        bot.load_extension(module)
        print(f"\nLoading Extension {module}")
    print("\nConnecting To The API")
    
bot.run(config["bottoken"])
