from discord.ext import commands
from discord_slash import cog_ext, SlashContext

def setup(bot):
    bot.add_cog(Carrot(bot))

class Carrot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="carrot", description="Somebody help me!")
    async def carrot(self, ctx: SlashContext):
        await ctx.send(":carrot:")