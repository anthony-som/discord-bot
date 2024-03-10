# Basic Discord Bot Using Slash Commands

This project is a simple Discord bot that utilizes slash commands. It's designed for those with a Discord Developer Badge, but it can be adapted for other uses as well.

## Installation

To get started, you will need to install the necessary Python libraries. Open your terminal and run the following commands:
```bash
pip install discord
pip install python-dotenv
```
## Configuration

Before you can run the bot, you need to set up your environment variables:

1. Create a `.env` file in the root directory of your project.
2. Add the following line to your `.env` file, replacing `discord-token` with your actual Discord bot token:

```env
DISCORD_TOKEN=discord-token
```

## Running the Bot

Once you have installed the dependencies and set up your `.env` file, you can start the bot by running:
```bash
python main.py
```
## Permissions

Ensure that your bot token has both `application.commands` and `bot` permissions under the OAuth2 settings in the Discord Developer Portal.

## Additional Notes

- Make sure you have Python installed on your system to run the bot.
- You may need to adjust the permissions in the Discord Developer Portal to suit your specific needs.

## Invite bot link
https://discord.com/oauth2/authorize?client_id=1216107511325786186&permissions=824633788480&scope=applications.commands+bot
