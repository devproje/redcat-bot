import discord, asyncio
from discord.ext import commands

def setup(bot):
    bot.add_cog(Mime(bot))

def image_selector(number):
    if number == None:
        return

    # TODO ADD SOME MEME IMAGE

class Mime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="짤")
    async def _meme(self, ctx, argument=None):
        if argument is None:
            # TODO GENERATED MEME COMMAND
            await ctx.send("None")