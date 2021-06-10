from sys import version
import discord, os, asyncio
from discord.ext import commands

token_path = "token.txt"
open_token = open(token_path, "r", encoding = "utf-8")
token = open_token.read().split()[0]

shell_version="v0.1.0"
version="v0.3.0"

bot = commands.Bot(command_prefix="\\", help_command=None)

def check_user(name, id):
    if name == "Project_TL":
        if id != "852387809481195520":
            return False

        else:
            return False
    else:
        return True

for filename in os.listdir("Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f"ProjectBot shell {shell_version}\n")
    print("Logined for ProjectBot shell!\n")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"ProjectBot {version}"))

    while True:
        shell_command = input("ProjectBot>")
        if shell_command == "reboot":
            exit()
        elif shell_command == "clear":
            os.system("clear")
        elif shell_command == "help":
            print("reboot")
            print("clear")
            print("help")
        else:
            print(f"{shell_command} command is unavaliable\n")

@bot.command(name="reload")
async def reload_commands(ctx, extension=None):
    print(f"name: {ctx.author.name}, id: {ctx.author.id}")
    os.system("git pull origin master")

    # if check_user(ctx.author.name, ctx.author.id):
    if extension is None:
        for filename in os.listdir("Cogs"):
            if filename.endswith(".py"):
                bot.unload_extension(f"Cogs.{filename[:-3]}")
                bot.load_extension(f"Cogs.{filename[:-3]}")

        await ctx.send(":white_check_mark: reload complete!")

    else:
        bot.unload_extension(f"Cogs.{extension}")
        bot.load_extension(f"Cogs.{extension}")
        await ctx.send(f":white_check_mark: **{extension}** has reloaded!")
    # else:
        # await ctx.send(":stop_sign: Error!")

bot.run(token)