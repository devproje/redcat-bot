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

    @cog_ext.cog_slash(name="setting", description="Owner's Settings!")
    async def avatar_image(self, ctx, *, sub_command, type):
        if ctx.author.id == self.owner_id:
            if sub_command == "avatar":
                if type == "daylight":
                    embed = (discord.Embed(title=":white_check_mark: **Done!**", description="CatBot's avatar mode is **daylight** mode!", color=self.embed_color)
                        .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))

                    with open('profile_image/daylight.png', 'rb') as profile_image:
                        await self.bot.user.edit(avatar=profile_image.read())
                
                    await ctx.send(embed=embed)
                
                elif type == "night":
                    embed = (discord.Embed(title=":white_check_mark: **Done!**", description="CatBot's avatar mode is **night** mode!", color=self.embed_color)
                        .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))
                
                    with open('profile_image/night.png', 'rb') as profile_image:
                        await self.bot.user.edit(avatar=profile_image.read())

                    await ctx.send(embed=embed)
            
                else:
                    embed = (discord.Embed(title=":no_entry: **Error!**", description=f"Invalid type `{type}`", color=self.embed_color)
                        .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))

                    await ctx.send(embed=embed)
            
            else:
                embed = (discord.Embed(title=":no_entry: **Error!**", description=f"Invalid subcommand `{sub_command}`", color=self.embed_color)
                    .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))

                await ctx.send(embed=embed)

        else:
            embed = (discord.Embed(title=":no_entry: **Error!**", description=f"You aren't bot owner!", color=self.embed_color)
                .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))

            await ctx.send(embed=embed)