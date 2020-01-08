import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print('------')
    print(bot.user)
    print(bot.user.id)
    print('------')

@bot.command()
async def roll(ctx):
    result = int(random.randint(1, 6))
    await ctx.send(result)

@bot.command()
async def ping(ctx):
    latency = str(round(bot.latency * 1000)) + "ms"
    await ctx.send(latency)

@bot.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)

bot.run('NDAzMzM2NzQzMzE2ODgxNDEw.XhVUDQ.nq-445l75ZhWaQFHUj0DOj0cu3I')
