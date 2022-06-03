import discord, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(".env")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=';', help_command=None, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

for filename in os.listdir("commands"):
    if filename.endswith(".py"):
        bot.load_extension(f"commands.{filename[:-3]}")

bot.run(os.getenv("TOKEN"))