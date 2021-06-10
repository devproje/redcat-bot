import discord, os, asyncio
from discord.ext import commands
from discord.ext.commands.core import command

def setup(bot):
    bot.add_cog(ProfileGrabber(bot))

class ProfileGrabber(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF

    @commands.command(name="profile")
    async def profile(self, ctx, member: discord.User = None or discord.User.mention == None):
        member = member or ctx.author
        embed = discord.Embed(title=f"**{member.display_name}#{member.discriminator}**'s Profile image!", color=self.embed_color)
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)