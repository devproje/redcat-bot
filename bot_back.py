import discord, os, asyncio
from discord import activity
from discord import embeds
from discord.ext import commands
from discord.ext.commands.help import HelpCommand

version = "v0.1.0"
personal_color = 0x75B8FF

token_path = "token.txt"
open_token = open(token_path, "r", encoding = "utf-8")
token = open_token.read().split()[0]

prefix = "\\"

game = discord.Game(f"ProjectBot-{version}")
client = commands.Bot(command_prefix=prefix, status=discord.Status.online, activity=game)

@client.event
async def on_ready():
    print("ProjectBot v0.1.0")

@client.command(name="ping")
async def ping(ctx):
    embed = discord.Embed(title=":ping_pong: Pong!", description=f"{round(client.latency * 1000)}ms", color=personal_color)
    await ctx.send(embed=embed)

@client.command(name="pong")
async def pong(ctx):
    embed=discord.Embed(title=":ping_pong: Ping!", description=f"{round(client.latency * 1000)}ms", color=personal_color)
    await ctx.send(embed=embed)

@client.command(name="reload")
async def reload(ctx, argument):
    if argument == "confirm":
        embed = discord.Embed(title=":repeat: Reload", description="**Please wait just more secs!**\nDiscord bot reloading...", color=0xFF0000)
        await ctx.channel.send(embed=embed)
        exit()

    else:
        embed = discord.Embed(title=":repeat: Reload", description=f"**{argument}** is not exist\nDiscord bot reloading...", color=0xFF0000)
        await ctx.channel.send(embed=embed)
        
    # embed = discord.Embed(title="Reload Error!", description="**You're not owner!**", color=0xFF0000)
    # wait ctx.channel.send(embed=embed)

@reload.error
async def reload_error(ctx, error):
    embed = discord.Embed(title="Reload Error!", description="**You must type confirm!**\nEx)\\reload confirm", color=0xFF0000)
    await ctx.channel.send(embed=embed)   

@client.command(name="carrot")
async def carrot(ctx):
    await ctx.send(":carrot:")

client.run(token)