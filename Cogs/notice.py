import discord, asyncio
from discord.ext import commands

def setup(bot):
    bot.add_cog(Notice(bot))

class Notice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF

    @commands.command(name="notice")
    async def notice(self, ctx, text):
        embed = discord.Embed(title=":satellite: Notice!", description=text, color=self.embed_color)
        embed.set_footer(text=f"{ctx.author.name}{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)