import os
import discord
from dotenv import load_dotenv
from discord import Intents, Client, Message, Interaction
from discord.ext import commands
from responses import get_response


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.tree.sync()
    await client.change_presence(activity=discord.activity.Game(name='Stocks'), status=discord.Status.do_not_disturb)
    print(f'{client.user} has connected to Discord!')
    
@client.command()
async def hello(ctx):
    await ctx.send('hey')
    
@client.tree.command(name='ping', description='Replies with ping in ms')
async def ping(interaction: Interaction):
    bot_latency = round(client.latency * 1000)
    await interaction.response.send_message(f'{bot_latency}ms')
    
    
client.run(TOKEN)
