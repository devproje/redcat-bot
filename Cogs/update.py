import discord, os, asyncio
from discord.ext import commands

def setup(bot):
    bot.add_cog(Update(bot))

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x00FF00

    @commands.command(name="update")
    async def update_code(self, ctx):
        if ctx.author.id != 415801068174180352:
            embed = discord.Embed(name=":stop_sign: Update fail!", description="You're not bot owner!", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)
        else:
            os.system("git pull origin master")
            embed = discord.Embed(name=":white_check_mark: Update Complete", description="Owner's code has successful updated!", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)