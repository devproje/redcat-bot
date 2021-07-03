import discord, os
from discord.ext import commands
from discord_slash import SlashContext, cog_ext

def setup(bot):
    bot.add_cog(Reload(bot))

class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.owner_id = 415801068174180352
        self.embed_color = 0x75B8FF

    @cog_ext.cog_slash(name="reload")
    async def reload_commands(self, ctx: SlashContext, extension=None):
        if ctx.author.id == self.owner_id:
            if extension is None:
                for filename in os.listdir("Cogs"):
                    if filename.endswith(".py"):
                        self.bot.unload_extension(f"Cogs.{filename[:-3]}")
                        self.bot.load_extension(f"Cogs.{filename[:-3]}")

                embed = discord.Embed(name=":white_check_mark: Done!", description="All command is reloaded!", color=self.embed_color)
                embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
                await ctx.channel.send(embed=embed)
            else:
                self.bot.unload_extension(f"Cogs.{extension}")
                self.bot.load_extension(f"Cogs.{extension}")
                embed = discord.Embed(name=":white_check_mark: Done!", description=f"{extension} is reloaded!", color=self.embed_color)
                embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
                await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(name=":stop_sign: Error", description="You're not bot owner!", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)