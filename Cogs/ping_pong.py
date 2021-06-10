import discord, os, asyncio
from discord import embeds
from discord.ext import commands

def setup(bot):
    bot.add_cog(PingPong(bot))

class PingPong(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF

    @commands.command(name="ping")
    async def ping(self, ctx):
        embed = discord.Embed(title=":ping_pong: Pong!", description=f"{round(self.bot.latency * 1000)}ms", color=self.embed_color)
        embed.set_footer(text=f"{ctx.author.name}{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name="pong")
    async def pong(self, ctx):
        embed=discord.Embed(title=":ping_pong: Ping!", description=f"{round(self.bot.latency * 1000)}ms", color=self.embed_color)
        embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)