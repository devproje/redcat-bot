from time import time
from discord.ext import commands
from inspect import getsource
from aioconsole import aexec
import discord, sys, os, subprocess

def setup(bot):
    bot.add_cog(Eval(bot))

class Eval(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="eval", pass_context=True)
    async def eval(self, ctx, *, code: str):
        code_file = open("code_space.py", mode="w", encoding="utf-8")
        code_file.write(code)
        code_file.close()

        file = open("code_space.py", mode="r", encoding="utf-8")

        source=file.read()
        file.close()
        
        cmd = ["python3.9", "code_space.py"]
        fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout
        data = fd_popen.read().strip()
        data_decode=data.decode("utf-8")
        fd_popen.close()
        embed=discord.Embed(title=":white_check_mark: **Python Eval Results**", description=f"**Source**:\n```py\n{source}\n```\n**Result**:\n```sh\n{data_decode}\n```")
        await ctx.send(embed=embed)