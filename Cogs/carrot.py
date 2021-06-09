import discord, asyncio
from discord.ext import commands

def setup(bot):
    bot.add_cog(Carrot(bot))

class Carrot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="carrot")
    async def carrot(self, ctx):
        await ctx.send(":carrot:")