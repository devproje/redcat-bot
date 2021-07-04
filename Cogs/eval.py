from time import time
from discord.ext import commands
from inspect import getsource
from aioconsole import aexec
import discord, sys, os

def setup(bot):
    bot.add_cog(Eval(bot))

class Eval(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="eval", pass_context=True)
    async def eval(self, ctx, *, code: str):
        code=f"""
        {code}
        """
        result=aexec(code)
        embed=discord.Embed(title=":white_check_mark: **Python Eval Results**", description=f"```py\n{result}\n```")
        await ctx.send(embed=embed)