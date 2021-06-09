import discord, os, asyncio
from discord import embeds
from discord.ext import commands
from discord.ext.commands import bot

def setup(bot):
    bot.add_cog(Reboot(bot))

class Reboot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0xFF0000

    @commands.command(name="reboot")
    async def reboot(self, ctx):
        embed = discord.Embed(title=":repeat: Reload", description="**Please wait just more secs!**\nDiscord bot reloading...", color=0xFF0000)
        await ctx.send(embed=embed)
        exit()