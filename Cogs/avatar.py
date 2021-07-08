import discord
from discord.ext import commands
from discord_slash import SlashContext, cog_ext

def setup(bot):
    bot.add_cog(Avatar(bot))

maintance_file="maintance.txt"
open_maintance=open(maintance_file, "r", encoding="utf-8")
maintance=open_maintance.read().split[0]

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0xED4245

        self.owner_id = 415801068174180352

    async def avatar_grabber(ctx, member):
        member = member or ctx.author
        embed = discord.Embed(title=f":frame_photo: **{member.display_name}#{member.discriminator}**'s Avatar!", color=self.embed_color)
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="avatar", description="You can grab target person's avatar image")
    async def avatar(self, ctx: SlashContext, member: discord.User = None or discord.User.mention == None):
        if maintance == "true":
            self.avatar_grabber(ctx, member)
        else:
            self.avatar_grabber(ctx, member)