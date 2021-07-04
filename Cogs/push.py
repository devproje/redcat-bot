import discord, os, subprocess
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

def setup(bot):
    bot.add_cog(Push(bot))

class Push(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.author_id = 415801068174180352

    @cog_ext.cog_slash(name="push")
    async def push_code(self, ctx: SlashContext):
        if ctx.author.id != self.author_id:
            embed = discord.Embed(title=f":stop_sign: **Error!**", description=f"You can push code!\nBecause you're not bot owner!")
            await ctx.send(embed=embed)
        else:
            cmd = ["sh", "~/project-bot_*/update.sh", "push"]
            fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout
            data = fd_popen.read().strip()
            data_decode=data.decode("utf-8")
            fd_popen.close()
            
            embed = (discord.Embed(title=f":white_check_mark: **Done!**", description=f"Instance code is pushed!\n```sh\n{data_decode}\n```")
                .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))
            await ctx.send(embed=embed)
