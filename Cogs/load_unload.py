import discord, os, asyncio
from discord import embeds
from discord.ext import commands
from discord.ext.commands import bot

def setup(bot):
    bot.add_cog(LoadUnload(bot))

class LoadUnload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="load")
    async def load(self, ctx, extension):
        # ctx.send("You're not bot owner!")
        self.bot.load_extension(f"Cogs.{extension}")
        await ctx.send(f":white_check_mark: {extension} has successful loaded!")


    @commands.command(name="unload")
    async def unload(self, ctx, extension):
        # await ctx.send("You're not bot owner!")
        self.bot.unload_extension(f"Cogs.{extension}")
        await ctx.send(f":stop_sign: {extension} has successful unloaded!")