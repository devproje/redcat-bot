import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

def setup(bot):
    bot.add_cog(Invite(bot))

class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0xED4245

    @cog_ext.cog_slash(name="invite", description="You can invite me!")
    async def carrot(self, ctx: SlashContext):
        embed = discord.Embed(title=":mailbox_with_mail: Invite Code!", description="https://projecttl.net/invite/redcat", color=self.embed_color)
        embed.set_footer(text=f"{ctx.author.name}{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        
        await ctx.send(embed=embed)