import discord
from discord.ext import commands
from aioconsole import aexec

def setup(bot):
    bot.add_cog(Eval(bot))

class Eval(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="eval")
    async def eval(self, ctx, *, type, code: str):
        if type == "py":
            result = await aexec(code)
            embed=discord.Embed(title=":white_check_mark: **Python Eval Results**", description=f"**Code**:\n```py\n{code}\n```\n**Result**:\n```sh\n{result}\n```")
            await ctx.send(embed=embed)