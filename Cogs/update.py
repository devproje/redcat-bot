import discord, os, asyncio
from discord.ext import commands

def setup(bot):
    bot.add_cog(bot)

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x00FF00

    @commands.command(name="update")
    async def update_code(self, ctx):
        os.system("git pull origin master")
        embed = discord.Embed(name=":white_check_mark: Update Complete", description="Owner's code has successful updated!", color=self.embed_color)
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)