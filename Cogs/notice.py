import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(Notice(bot))

class Notice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF

        self.author_id = 415801068174180352

    @commands.command(name="notice")
    async def notice(self, ctx, text):
        if ctx.author.id != self.author_id:
            embed = discord.Embed(title=":stop_sign: **Error!**", description="You're not bot owner!", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=":satellite: **Notice!**", description=text, color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)