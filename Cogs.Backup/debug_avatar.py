import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

def setup(bot):
    bot.add_cog(OwnerSetting(bot))

class OwnerSetting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.embed_color = 0xED4245
        self.owner_id = 415801068174180352

    @cog_ext.cog_slash(name="set_avatar", description="This is test command!")
    async def avatar_setting(self, ctx, *, extention, type):
        if ctx.author.id == self.owner_id:
            if not extention == None:
                if type == None:
                    embed = (discord.Embed(title=":no_entry: **Error**", description="Type must not None", color=self.embed_color)
                        .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))
                    await ctx.send(embed=embed)

                else:
                    embed = (discord.Embed(title=":white_check_mark: **Done!**", description=f"CatBot's avatar mode is {extention} **{type}** mode!", color=self.embed_color)
                        .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))

                    with open(f'profile_image/{extention}/{type}.png', 'rb') as profile_image:
                        await self.bot.user.edit(avatar=profile_image.read())
                
                    await ctx.send(embed=embed)
            else:
                embed = (discord.Embed(title=":no_entry: **Error**", description="Extention must not None", color=self.embed_color)
                    .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))
                await ctx.send(embed=embed)

        else:
            embed = (discord.Embed(title=":no_entry: **Error!**", description="You're not bot owner!", color=self.embed_color)
                .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))

            await ctx.send(embed=embed)