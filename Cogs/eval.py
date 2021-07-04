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
        self.author_id = 415801068174180352
    
    @commands.command(name="eval", pass_context=True)
    async def eval(self, ctx, *, code: str):
        if ctx.author.id != self.author_id:
            return None
        else:
            code_file = open("code_space.py", mode="w", encoding="utf-8")
            (code_file.write(code)
                .close())

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