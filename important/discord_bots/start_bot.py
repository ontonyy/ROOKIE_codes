import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
TOKEN = os.getenv('DISCORD_TOKEN')
# await attribute would be not first before async in def

client = commands.Bot(command_prefix="!")


@client.command()
async def hello(ctx, *args):
    for arg in args:
        await ctx.send(arg)


client.run(TOKEN)
