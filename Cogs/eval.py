from discord.ext import commands
from discord_slash import SlashContext, cog_ext
from aioconsole import aexec

def setup(bot):
    bot.add_cog(Eval(bot))

class Eval(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="eval", description="Eval code")
    async def eval(self, ctx: SlashContext, *, type, code):
        if type == "py":
            await aexec(code)