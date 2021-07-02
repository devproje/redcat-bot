import discord, os, asyncio
from discord.ext import commands
from discord_slash import SlashCommand

def setup(bot):
    bot.add_cog(Test(bot))

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @SlashCommand.slash(name="test", description="This is just a test command, nothing more.")
    async def test(self, ctx):
        await ctx.send(content="Hello World!")