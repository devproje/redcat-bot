import discord, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(".env")

class RedCat(discord.Client):
    async def on_ready(self):
        print(f'Logged in as Bot')

intents = discord.Intents.default()
bot = RedCat(intents=intents)

bot.run(os.getenv("TOKEN"))