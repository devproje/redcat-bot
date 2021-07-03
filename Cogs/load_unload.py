import discord, os, asyncio
from discord import embeds
from discord.ext import commands
from discord.ext.commands import bot
from discord_slash import SlashContext, cog_ext

def setup(bot):
    bot.add_cog(LoadUnload(bot))

class LoadUnload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.author_id = 415801068174180352

    @cog_ext.cog_slash(name="load")
    async def load(self, ctx: SlashContext, extension):
        if ctx.author.id != self.author_id:
            embed = discord.Embed(title=f":stop_sign: **Error!**", description=f"You can't loaded **{extension}**!\nBecause you're not bot owner!")
            await ctx.send(embed=embed)
        else:
            self.bot.load_extension(f"Cogs.{extension}")
            embed = discord.Embed(title=f":white_check_mark: **Done!**", description=f"**{extension}** has successful loaded!")
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)


    @cog_ext.cog_slash(name="unload")
    async def unload(self, ctx: SlashContext, extension):
        if ctx.author.id != self.author_id:
            embed = discord.Embed(title=f":stop_sign: **Error!**", description=f"You can't unloaded **{extension}**!\nBecause you're not bot owner!")
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            self.bot.unload_extension(f"Cogs.{extension}")
            embed = discord.Embed(title=f":white_check_mark: **Done!**", description=f"**{extension}** has successful unloaded!")
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
