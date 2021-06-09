import discord, os, asyncio
from discord.ext import commands

token_path = "token.txt"
open_token = open(token_path, "r", encoding = "utf-8")
token = open_token.read().split()[0]

bot = commands.Bot(command_prefix="\\", help_command=None)

for filename in os.listdir("Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print("Logined!")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("ProjectBot v0.2.0"))

@bot.command()
async def load(ctx, extension):
    if ctx.author.guild_permissions.administrator == False:
        ctx.send('권한이 없습니다.')
    else:
        bot.load_extension(f"Cogs.{extension}")
        await ctx.send(f":white_check_mark: {extension}을(를) 로드했습니다!")


@bot.command()
async def unload(ctx, extension):
    if ctx.author.guild_permissions.administrator == False:
        await ctx.send('권한이 없습니다.')
    else:
        bot.unload_extension(f"Cogs.{extension}")
        await ctx.send(f":white_check_mark: {extension}을(를) 언로드했습니다!")


@bot.command(name="reload")  # 1
async def reload_commands(ctx, extension=None):
    if extension is None:  # 3
        for filename in os.listdir("Cogs"):
            if filename.endswith(".py"):
                bot.unload_extension(f"Cogs.{filename[:-3]}")
                bot.load_extension(f"Cogs.{filename[:-3]}")
                
        await ctx.send(":white_check_mark: reload complete!")

    else:  # 4
        bot.unload_extension(f"Cogs.{extension}")  # 5
        bot.load_extension(f"Cogs.{extension}")
        await ctx.send(f":white_check_mark: {extension} has reloaded!")    

bot.run(token)