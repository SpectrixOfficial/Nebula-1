import discord, asyncio, json, time, io, traceback, inspect, textwrap, datetime
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

    @commands.command()
    async def _eval(self, ctx, *, body: str):
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
    
def setup(bot):
    bot.add_cog(Developers(bot))