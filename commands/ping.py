import discord, os
from discord.ext import commands

class Ping(commands.Cog):
    __doc__ = "API 레이턴시를 확인합니다."
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = int(os.getenv("COLOR"), 16)
    
    @commands.command(name="ping", help="구문이 없습니다.")
    async def ping(self, ctx):
        embed = discord.Embed(title=":ping_pong: **Pong!**", description=f"{round(self.bot.latency * 1000)}ms", color=self.embed_color)
        embed.set_footer(text=f"{ctx.author.name}{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)

        await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(Ping(bot))
