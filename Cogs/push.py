import discord, os, asyncio
from discord.ext import commands

def setup(bot):
    bot.add_cog(Push(bot))

class Push(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.author_id = 415801068174180352

    @commands.command(name="push")
    async def push_code(self, ctx):
        if ctx.author.id != self.author_id:
            embed = discord.Embed(title=f":stop_sign: **Error!**", description=f"You can push code!\nBecause you're not bot owner!")
            await ctx.send(embed=embed)
        else:
            log = os.system("git push origin master")
            embed = (discord.Embed(title=f":white_check_mark: **Done!**", description=f"Instance code is pushed!\n```sh{str(log)}\n```")
                .add_field(name="", value="", inline=True))
            await ctx.send(embed=embed)