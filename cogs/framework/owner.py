import discord, asyncio, json, time, io, traceback, inspect, textwrap, datetime, os
from time import ctime
from contextlib import redirect_stdout
from discord.ext import commands

with open("data.json") as f:
    config = json.load(f)

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
        return ctx.author.id == config["bot"]["developer"]["enternewname"] or ctx.author.id == config["bot"]["developer"]["banii"]

    def get_syntax_error(self, e):
        if e.text is None:
            return f'```py\n{e.__class__.__name__}: {e}\n```'
        return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'

    @commands.command()
    async def eval(self, ctx, *, body: str):
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
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
            try:
                await ctx.message.add_reaction(':tickNo:483288678437879808')
            except:
                pass
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction(':tickYes:483288647823523841')
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
    

    
def setup(bot):
    bot.add_cog(Developers(bot))