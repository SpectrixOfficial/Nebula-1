import discord, asyncio, json, time, io, traceback, inspect, textwrap, datetime, os, sqlite3
from time import ctime
from contextlib import redirect_stdout
from discord.ext import commands

class Developers:
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()

    def cleanup_code(self, message):
        if message.startswith('```') and message.startswith("```"):
            return "\n".join(message.split('\n')[1:-1])
        return message.strip(' \n')
    
    async def __local_check(self, ctx):
        return await self.bot.is_owner(ctx.author)

    def get_syntax_error(self, e):
        if e.text is None:
            return f'```py\n{e.__class__.__name__}: {e}\n```'
        return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'

    @commands.command(hidden=True)
    async def eval(self, ctx, *, body : str):
        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}```')
            try:
                await ctx.message.add_reaction(':tickNo:490607198443929620')
            except:
                pass
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction(':tickYes:490607182010777620')
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                self._last_result = ret
                await ctx.send(f'```py\n{value}{ret}\n```')

    @commands.command(aliases=['rl'])
    async def reload(self, ctx, cog):
        try:
            self.bot.unload_extension(f"cogs.{cog}")
            self.bot.load_extension(f"cogs.{cog}")
            await ctx.send(f"***Reloaded Cog `cogs.{cog}`***")
        except Exception as e:
            await ctx.send(f"```fix\n{e}\n```")
    
    @commands.command(aliases=['l'])
    async def load(self, ctx, cog):
        try:
            self.bot.load_extension(f"cogs.{cog}")
            await ctx.send(f"***Loaded Cog `cogs.{cog}`***")
        except Exception as e:
            await ctx.send(f"```fix\n{e}\n```")

    @commands.command(aliases=['ul'])
    async def unload(self, ctx, cog):
        self.bot.unload_extension(f"cogs.{cog}")
        await ctx.send(f"***Unloaded Cog `cogs.{cog}`***")

    @commands.group(invoke_without_command=True)
    async def devtools(self, ctx):
        await ctx.send("Developer Tools For Use Of the Bot In General")

    @devtools.command()
    async def presence(self, ctx, typ : int, *, presencegame=None):
        if presencegame is None:
            await self.bot.change_presence(activity=discord.Activity(name=f".help in {len(self.bot.guilds)} Servers", url="https://www.twitch.tv/Enter%20New%20Name", type=1))
            await ctx.send(f"Changed Presence to `Default Presence`")
        else:
            await self.bot.change_presence(activity=discord.Activity(name=f"{presencegame} | {len(self.bot.guilds)} Guilds!", type=typ, url="https://www.twitch.tv/Enter%20New%20Name"))
            if typ == 0:
                typtype = "Playing"
            elif typ == 1:
                typtype = "Streaming"
            elif typ == 2:
                typtype = "Listening to"
            elif typ == 3:
                typtype = "Watching"
            else:
                typtype = "Unknown Type"
            await ctx.send(f"Changed Presence To `{typtype}` | `{typ}`\nGame Status: `{presencegame} | {len(self.bot.guilds)} Guilds!`")

    @devtools.command(aliass=['logout'])
    async def logoff(self, ctx):
        await ctx.send("Logged Out")
        await self.bot.logout()
    
def setup(bot):
    bot.add_cog(Developers(bot))