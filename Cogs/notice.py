import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

def setup(bot):
    bot.add_cog(Notice(bot))

class Notice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0xED4245

        self.author_id = 415801068174180352

    @cog_ext.cog_slash(name="notice", description="TEST FUNCTION!")
    async def notice(self, ctx: SlashContext, text: str):
        if ctx.author.id != self.author_id:
            embed = discord.Embed(title=":stop_sign: **Error!**", description="You're not bot owner!", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=":satellite: **Notice!**", description=f"{text}", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)