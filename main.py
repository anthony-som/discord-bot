import os
import discord
from dotenv import load_dotenv
# Corrected import path for Interaction
from discord import app_commands
from discord.ext import commands

import requests
import json
from datetime import datetime
import pytz
from pytz import timezone

import time

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Intents should be explicitly defined for what your bot needs. For a basic bot, not all intents may be necessary.
intents = discord.Intents.all()

client = commands.Bot(command_prefix='.', intents=intents)
est = pytz.timezone('US/Eastern')

@client.event
async def on_ready():
    await client.tree.sync()
    await client.change_presence(activity=discord.Game(name='Eating fries'), status=discord.Status.do_not_disturb)
    print(f'{client.user} has connected to Discord!')

@client.command()
async def hello(ctx):
    await ctx.send('hey')
    
    
@client.tree.command(name='time', description='Replies with time')
async def time(interaction: discord.Interaction):
    current_time = datetime.now(est)
    formatted_datetime = current_time.strftime('%B %d, %Y %I:%M %p')  # This formats the datetime as "Month Day, Year Hour:Minute AM/PM"
    await interaction.response.send_message(f'Current date and time: {formatted_datetime}')

    
# Use app_commands for interaction-based commands
@client.tree.command(name='ping', description='Replies with ping in ms')
async def ping(interaction: discord.Interaction):
    bot_latency = round(client.latency * 1000)
    await interaction.response.send_message(f'{bot_latency}ms')

@client.tree.command(name='burger', description='Replies with burger deal')
async def burger(interaction: discord.Interaction):
    
    response = requests.get('https://api-web.nhle.com/v1/club-schedule/TOR/week/now') # Get schedule for the Toronto Maple Leafs

    current_date = datetime.now(est).date() # get today's date

    json_data = response.json() if response and response.status_code == 200 else None # get the json data from the response

    def game_check():
        if json_data and 'games' in json_data:
            for game in json_data['games']:
                game_date = datetime.strptime(game['gameDate'], '%Y-%m-%d').date()
                if game_date == current_date:
                    return True
                else:
                    return False

    game_today = game_check()

    if game_today:
        message = 'There is a $2 Teen burger on the A&W App, go get it!'
    else:
        message = 'There is no teen burger deal today!'
    
    await interaction.response.send_message(message)


client.run(TOKEN)