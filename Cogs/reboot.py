import discord
from discord import embeds
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

def setup(bot):
    bot.add_cog(Reboot(bot))
    bot.add_cog(Slash(bot))

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.slash = SlashCommand(bot, override_type=True)
        # Cog is only supported by commands ext, so just skip checking type.

        @self.slash.slash(name="test")
        async def _test(ctx: SlashContext):
            await ctx.send(content="Hello, World!")

    def cog_unload(self):
        self.slash.remove()

class Reboot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.slash = SlashCommand(bot, override_type=True)
        self.embed_color = 0xFF0000

        self.author_id = 415801068174180352

        @self.slash.slash(name="reboot")
        async def reboot(self, ctx: SlashContext):
            if ctx.author.id == self.author_id:
                embed = discord.Embed(title=":repeat: Reboot", description="**Please wait just more secends!**\nDiscord bot rebooting...", color=0xFF0000)
                embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                exit()
            else:
                embed = discord.Embed(title=":repeat: Reboot Error!", description="**You're not bot owner!**", color=0xFF0000)
                embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)