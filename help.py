import discord, asyncio
from discord import embeds
from discord.ext import commands

def setup(bot):
    bot.add_cog(Help(bot))

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF

    @commands.command(name="phelp")
    async def help(self, ctx):
        embed = discord.Embed(title=":dart: **Help**", description="", color=self.embed_color)
        embed.add_field(name="`\\help`", value="Open help embed", inline=True)
        embed.add_field(name="`\\ping`", value="ping with your bot", inline=True)
        embed.add_field(name="`\\pong`", value="pong with your bot", inline=True)
        embed.add_field(name="`\\carrot`", value="Help! :carrot:", inline=True)
        embed.add_field(name="`\\reload`", value="Reload command", inline=True)
        embed.add_field(name="`\\reboot`", value="Reboot command **Update bot only**", inline=True)

        await ctx.send(embed=embed)