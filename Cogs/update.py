import discord, os, subprocess
from discord.ext import commands
from discord_slash import SlashContext, cog_ext

def setup(bot):
    bot.add_cog(Update(bot))

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x00FF00
        self.author_id = 415801068174180352

    @cog_ext.cog_slash(name="update")
    async def update_code(self, ctx: SlashContext):
        if ctx.author.id != self.author_id:
            embed = discord.Embed(name=":stop_sign: Update fail!", description="You're not bot owner!", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)
        else:
            cmd = ["git", "pull", "origin", "master"]
            fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout
            data = fd_popen.read().strip()
            data_conv = data.decode('utf-8')
            fd_popen.close()

            embed = (discord.Embed(name=":white_check_mark: Update Complete", description="Owner's code has successful updated!", color=self.embed_color)
                .add_field(name="Git Status", value=f"```sh\n{data_conv}\n```", inline=False))
        
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)