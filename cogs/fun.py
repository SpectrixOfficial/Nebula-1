import discord, asyncio, json, random, math, os, aiohttp
from discord.ext import commands
from discord.ext.commands import clean_content

with open("database/data.json") as file:
    config = json.load(file)

class FunCommands:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print("FunCommands Is Loaded")

    @commands.command()
    async def rps(self, ctx, choice):
        botChoice = random.choice(['rock', 'paper', 'scissors'])

        async def userWins():
            await ctx.send(f"I choose... **{botChoice}**. You win! ***{choice} beats {botChoice}!***")

        async def botWins():
            await ctx.send(f"I choose... **{botChoice}**. I win! ***{botChoice} beats {choice}!***")

        if choice == botChoice:
            await ctx.send(f"***Tie!*** We both used {botChoice}!")

        elif choice == "rock":
            if botChoice == "paper":
                await botWins()
            else:
                await userWins()
        elif choice == "paper":
            if botChoice == "scissors":
                await botWins()
            else:
                await userWins()    
        elif choice == "scissors":
            if botChoice == "paper":
                await userWins()
            else:
                await botWins()

    @commands.command()
    async def poll(self, ctx, * ,PollMessage : clean_content):
        embed = discord.Embed(color=ctx.author.color)
        embed.set_author(icon_url=ctx.author.avatar_url, name=f"Poll Made By {ctx.author}")
        embed.add_field(name="\uFEFF", value=PollMessage)
        pollmsg = await ctx.send(embed=embed)
        await ctx.message.delete()
        try:
            await pollmsg.add_reaction(emoji=":tickYes:490607182010777620")
            await pollmsg.add_reaction(emoji=":tickNo:490607198443929620")
        except:
            await ctx.send("***Make Sure I have `add_reactions` so I can make the poll***")

    @commands.guild_only()
    @commands.command()
    async def perms(self, ctx, *, user : discord.Member=None):
        if not user:
            user = ctx.author
        permissions = '\n'.join(permission for permission, value in user.guild_permissions if value)
        embed = discord.Embed(color=user.color)
        embed.set_author(name=str(user))
        embed.add_field(name="\uFEFF", value=permissions)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(icon_url=ctx.guild.icon_url, text=ctx.guild)
        await ctx.send(embed=embed, content=None)
    

    @commands.group(aliases=['gh'])
    async def github(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(color=discord.Color(value=0x1c407a))
            embed.set_author(icon_url=config['urls']['transparentgithubimg'], name="GitHub Commands")
            embed.add_field(name="Search User", value="e.g `.github user <user>`", inline=False)
            embed.add_field(name="Search Repository", value="e.g `.github repo <owner>/<reponame>`", inline=False)
            embed.set_footer(text="GitHub Commands In Testing")
            await ctx.send(embed=embed)

    @github.command()
    async def user(self, ctx, *, githubacct):
        try:           
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api.github.com/users/{githubacct}") as b:
                    a = await b.json()
                    #Prepares Things
                    username = a['login']
                    repos = a['public_repos']
                    following = a['following']
                    followers = a['followers']
                    pfp = a['avatar_url']
                    bio = a['bio']
                    repolist = f"https://github.com/{username}?tab=repositories"
                    profilepage = a['html_url']
                    emb = discord.Embed(color=discord.Color(value=0x1c407a))
                    emb.set_author(name=f"GitHub User: {username} ({a['name']})",url=profilepage, icon_url=config['urls']['transparentgithubimg'])
                    emb.set_thumbnail(url=pfp)
                    emb.add_field(name="Repositories:", value=f"{repos} Public Repos", inline=False)
                    emb.add_field(name="Biography", value=bio)
                    emb.add_field(name="Popularity:", value=f"Following: {following}\nFollowers: {followers}", inline=False)
                    emb.add_field(name=f"Links", value=f"[Repositories]({repolist})")
                    await ctx.send(embed=emb)
        except:
            await ctx.send(embed=discord.Embed(description=f"***`{githubacct}` isn't a Valid Account, if So, Try Again Later***", color=discord.Color(value=0x1c407a)))

    @github.command(aliases=['repository'])
    async def repo(self, ctx, * , reqresult):
        try:
            async with aiohttp.ClientSession() as api:
                async with api.get(f"https://api.github.com/repos/{reqresult}") as resp:
                    json = await resp.json()
                    emb = discord.Embed(color=discord.Color(value=0x1c407a))
                    emb.set_author(icon_url=config['urls']['transparentgithubimg'],name=f"{json['full_name']}", url=json['html_url'])
                    emb.add_field(name="Description:", value=json['description'], inline=False)
                    emb.add_field(name="Mostly Used Language:", value=json['language'], inline=False)
                    emb.add_field(name="Stargazers:", value=json['stargazers_count'], inline=False)
                    emb.add_field(name="Forks:", value=json['forks_count'], inline=False)
                    emb.add_field(name="Watching:", value=json['watchers_count'], inline=False)
                    await ctx.send(embed=emb)
        except:
            await ctx.send(embed=discord.Embed(description=f"***`{reqresult}` isn't a Valid Repo, if So, Try Again Later***", color=discord.Color(value=0x1c407a)))
                

def setup(bot):
    bot.add_cog(FunCommands(bot))