import discord, asyncio
from discord import embeds
from discord.ext import commands

def setup(bot):
    bot.add_cog(Help(bot))

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF

    @commands.command(name="help")
    async def help(self, ctx):
        embed = discord.Embed(title=":dart: **Help**", description="**This is command list**", color=self.embed_color)
        embed.add_field(name="`\\help`", value="Open help embed", inline=True)
        embed.add_field(name="`\\ping`", value="ping with your bot", inline=True)
        embed.add_field(name="`\\pong`", value="pong with your bot", inline=True)
        embed.add_field(name="`\\carrot`", value="Help! :carrot:", inline=True)
        embed.add_field(name="`\\wincho <action>`", value="you can broken wintchoco", inline=True)
        embed.add_field(name="`\\윈초 <action>`", value="당신은 윈초를 괴롭힐 수 있습니다", inline=True)
        embed.add_field(name="`\\version`", value="You can see this bot version", inline=True)

        if ctx.author.id != 415801068174180352:
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        else:
            embed.add_field(name="**Bot owner command**", value="This command only can use with bot owner", inline=False)
            embed.add_field(name="`\\reboot`", value="Reboot command\n**Update bot only**", inline=True)
            embed.add_field(name="`\\reload`", value="Reload command", inline=True)
            embed.add_field(name="`\\notice <text>`", value="notice command", inline=True)
            embed.add_field(name="`\\load <extension_name>`", value="You can load command", inline=True)
            embed.add_field(name="`\\unload <extension_name>`", value="You can unload command", inline=True)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        
        await ctx.channel.send(embed=embed)