import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

def setup(bot):
    bot.add_cog(ProfileGrabber(bot))

class ProfileGrabber(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF

    @cog_ext.cog_slash(name="profile", description="You can grab target person's avatar image")
    async def profile(self, ctx: SlashContext, member: discord.User = None or discord.User.mention == None):
        member = member or ctx.author
        embed = discord.Embed(title=f"**{member.display_name}#{member.discriminator}**'s Profile image!", color=self.embed_color)
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)