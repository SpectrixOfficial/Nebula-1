import discord, asyncio, json, pkg_resources, time, datetime, aiohttp, logging, aiosqlite, sys
from discord.ext import commands
from time import ctime

with open("database/data.json") as f:
    config = json.load(f)


class Nebula_Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(config['prefix']),
                         case_insensitive=True)


    async def presencehandler(self):
        header = {"Authorization" : config["dbltoken"]}
        payload = {"server_count"  : len(self.guilds)}
        await self.change_presence(activity=discord.Activity(name=f".help in {len(self.guilds)} Servers!", url="https://www.twitch.tv/EnterNewName", type=1))
        async with aiohttp.ClientSession() as session:
            await session.post("https://discordbots.org/bot/487164011683774464/stats", data=payload, headers=header)


    async def on_guild_remove(self, guild):
        try:
            await self.presencehandler()
        except Exception as e:
            await self.presencehandler()
            print(f"Having A Problem With Loading The presence_handler\nHeres The Error: {e}")  

    async def on_ready(self):
        await  self.presencehandler()
        print("========================\nConnected To Discord API")
        print("========================\nStats:\n")
        print("Discord.py Version : " + pkg_resources.get_distribution("discord.py").version)
        print(f"{self.user} Is Online")
        print(f"Guild Count : {len(self.guilds)}\n")

    async def on_guild_join(self, guild):
        try:
            self.presencehandler()
        except Exception as e:
            self.presencehandler()
            print(f"Having A Problem With Loading The presence_handler\nHeres The Error: {e}")            
        try:
            embed = discord.Embed(color=discord.Color(value=0x1c407a))
            embed.set_author(name="Thanks For Inviting Nebula")
            embed.add_field(name="My Prefix is `.`", value=f"[Support](https://enternewname.me/redirects/support)", inline=False)
            embed.add_field(name="Need Help?", value="[Click here](https://enternewname.me/nebula/commands)", inline=False)
            embed.add_field(name="Logging Channel Requirement", value="***#mod-log***", inline=False)
            await guild.system_channel.send(embed=embed)
        except:
            pass
            

    def intiate_startup(self):
        self.remove_command('help')
        cogs = config["cogs"]
        try:
            for module in cogs:
                self.load_extension(module)
                print(f"\nLoading Extension {module}")
            print("\nConnecting To The API")
            super().run(config["bottoken"])
        except Exception as e:
            print(f"\n{e}\n")

if __name__ == "__main__":
    Nebula_Bot().intiate_startup()
