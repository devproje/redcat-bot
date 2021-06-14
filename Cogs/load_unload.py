import discord, os, asyncio
from discord import embeds
from discord.ext import commands
from discord.ext.commands import bot

def setup(bot):
    bot.add_cog(LoadUnload(bot))

class LoadUnload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.author_id = 415801068174180352

    @commands.command(name="load")
    async def load(self, ctx, extension):
        if ctx.author.id != self.author_id:
            embed = discord.Embed(title=f":stop_sign: **Error!**", description=f"You can't loaded {extension}!\nBecause you're not bot owner!")
            await ctx.send(embed=embed)
        else:
            self.bot.load_extension(f"Cogs.{extension}")
            embed = discord.Embed(title=f":white_check_mark: **Done!**", description=f"{extension} has successful loaded!")
            await ctx.send(embed=embed)


    @commands.command(name="unload")
    async def unload(self, ctx, extension):
        if ctx.author.id != self.author_id:
            embed = discord.Embed(title=f":stop_sign: **Error!**", description=f"You can't unloaded {extension}!\nBecause you're not bot owner!")
            await ctx.send(embed=embed)
        else:
            self.bot.unload_extension(f"Cogs.{extension}")
            embed = discord.Embed(title=f":white_check_mark: **Done!**", description=f"{extension} has successful unloaded!")
            await ctx.send(embed=embed)
