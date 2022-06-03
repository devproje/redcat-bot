from discord.ext import commands

class Carrot(commands.Cog):
    __doc__ = "곤란한 상황(?)이 있을때 사용하세요"
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="carrot", help="구문이 없습니다.")
    async def carrot(self, ctx):
        await ctx.send(":carrot:")

def setup(bot):
    bot.add_cog(Carrot(bot))