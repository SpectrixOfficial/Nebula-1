import discord, asyncio, json, pkg_resources, time, datetime, aiohttp, logging, aiosqlite
from discord.ext import commands
from time import ctime

with open("database/data.json") as f:
    config = json.load(f)

startup = datetime.datetime.utcnow()
class Nebula(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(config['defaultprefix']),
                         case_insensitive=True,
                         clean_content=True)
        self.remove_command('help')


    async def on_ready(self):
        print("\n========================\nConnected To Discord API")
        print("========================\nStats:\n")
        print("Discord.py Version : " + pkg_resources.get_distribution("discord.py").version)
        print(f"{self.user} Is Online")
        print(f"Guild Count : {len(self.guilds)}\n")
        while True:
            header = {"Authorization" : config["dbltoken"]}
            payload = {"server_count"  : len(self.guilds)}
            await self.change_presence(activity=discord.Activity(name=f".help in {len(self.guilds)} Servers!", url="https://www.twitch.tv/EnterNewName", type=1))
            async with aiohttp.ClientSession() as session:
                await session.post("https://discordbots.org/bot/487164011683774464/stats", data=payload, headers=header)
            await asyncio.sleep(60)

    async def on_guild_join(self, guild):           
        try:
            embed = discord.Embed(color=discord.Color(value=0x1c407a))
            embed.set_author(name="Thanks For Inviting Nebula")
            embed.add_field(name="My Prefix is `.`", value=f"[Support](https://enternewname.me/redirects/support)", inline=False)
            embed.add_field(name="Need Help?", value="[Click here](https://enternewname.me/nebula/commands)", inline=False)
            embed.add_field(name="Logging Channel Requirement", value="***#mod-log***", inline=False)
            embed.set_footer(text=f"Thanks To You, Nebula is has now {len(self.guilds)} servers!", icon_url=guild.icon.avatar_url)
            await guild.system_channel.send(embed=embed)
        except:
            pass
            
                
    async def on_message(self, msg):
        if msg.content == f"{config['defaultprefix']}uptime":
            delta_uptime = datetime.datetime.utcnow() - startup
            hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            days, hours = divmod(hours, 24)
            await msg.channel.send(f"I have been running for **{days}** days, **{hours}** hours, **{minutes}** minutes, **{seconds}** seconds!")

    def initial_start(self):
        cogs = config["cogs"]
        try:
            for module in cogs:
                self.load_extension(module)
                print(f"\nLoading Extension {module}")
            print("\nConnecting To The API")
            super().run(config['bottoken'])
        except Exception as error:
            print(f"{self.user} Could Not Be Loaded\nError\n\n{error}")

if __name__ == '__main__':
    Nebula().initial_start()