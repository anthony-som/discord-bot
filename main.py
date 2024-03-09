import os
import discord
from dotenv import load_dotenv
# Corrected import path for Interaction
from discord import app_commands
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Intents should be explicitly defined for what your bot needs. For a basic bot, not all intents may be necessary.
intents = discord.Intents.default()

client = commands.Bot(command_prefix='.', intents=intents)

@client.event
async def on_ready():
    await client.tree.sync()
    await client.change_presence(activity=discord.Game(name='Stocks'), status=discord.Status.do_not_disturb)
    print(f'{client.user} has connected to Discord!')

@client.command()
async def hello(ctx):
    await ctx.send('hey')

# Use app_commands for interaction-based commands
@client.tree.command(name='ping', description='Replies with ping in ms')
async def ping(interaction: discord.Interaction):
    bot_latency = round(client.latency * 1000)
    await interaction.response.send_message(f'{bot_latency}ms')

client.run(TOKEN)
