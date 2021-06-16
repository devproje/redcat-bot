import discord
from discord import embeds
from discord.ext import commands

def setup(bot):
    bot.add_cog(Reboot(bot))

class Reboot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0xFF0000

        self.author_id = 415801068174180352

    @commands.command(name="reboot")
    async def reboot(self, ctx):
        if ctx.author.id == self.author_id:
            embed = discord.Embed(title=":repeat: Reboot", description="**Please wait just more secends!**\nDiscord bot rebooting...", color=0xFF0000)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            exit()
        else:
            embed = discord.Embed(title=":repeat: Reboot Error!", description="**You're not bot owner!**", color=0xFF0000)
            await ctx.send(embed=embed)