import discord_slash
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.context import SlashContext

def setup(bot):
    bot.add_cog(Test(bot))

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="test_ping")
    async def ping(self, ctx: SlashContext):
        await ctx.send(content="Pong!")