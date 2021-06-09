import discord, os, asyncio
from discord import embeds
from discord.ext import commands

def setup(bot):
    bot.add_cog(PingPong(bot))

class PingPong(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(ctx):
        embed = discord.Embed(title=":ping_pong: Pong!", description=f"{round(client.latency * 1000)}ms", color=personal_color)
        await ctx.send(embed=embed)

    @commands.command(name="pong")
    async def pong(ctx):
        embed = discord.Embed(title="::")