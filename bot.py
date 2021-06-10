import discord, os, asyncio
from discord.ext import commands
from get_owner import check_id

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
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("ProjectBot v0.2.1"))

@bot.command(name="reload")
async def reload_commands(ctx, extension=None):
    print(f"name: {ctx.author.name}, id: {ctx.author.id}")

    if check_id(ctx.author.name, ctx.author.id):
        if extension is None:
            for filename in os.listdir("Cogs"):
                if filename.endswith(".py"):
                    bot.unload_extension(f"Cogs.{filename[:-3]}")
                    bot.load_extension(f"Cogs.{filename[:-3]}")

            await ctx.send(":white_check_mark: reload complete!")

        else:
            bot.unload_extension(f"Cogs.{extension}")
            bot.load_extension(f"Cogs.{extension}")
            await ctx.send(f":white_check_mark: {extension} has reloaded!")    
    else:
        await ctx.send(":stop_sign: Error!")

bot.run(token)