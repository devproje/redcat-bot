import discord, os
from discord.ext import commands

class Help(commands.Cog):
    __doc__ = "도움말을 엽니다."
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = int(os.getenv("COLOR"), 16)
    @commands.command(name="help", help="<command> - 이 봇의 명령어중 하나를 입력하는 곳 입니다.")
    async def help(self, ctx, *input):
        if not input:
            embed = discord.Embed(title=':dart: **Help**', description=f'`;help <command>`로 해당 명령어의 설명을 보실 수 있습니다.')

            cogs_desc = ''
            for cog in self.bot.cogs:
                cogs_desc += f'`;{cog.lower()}` {self.bot.cogs[cog].__doc__}\n'

            embed.add_field(name='Commands', value=cogs_desc, inline=False)

        elif len(input) == 1:
            for cog in self.bot.cogs:
                if cog.lower() == input[0].lower():
                    embed = discord.Embed(title=f':notepad_spiral: {cog}', description=self.bot.cogs[cog].__doc__)
                    for command in self.bot.get_cog(cog).get_commands():
                        if not command.hidden:
                            embed.add_field(name=f"`;{command.name}`", value=command.help, inline=False)
                    break
            else:
                embed = discord.Embed(title=":no_entry: **Error!**", description=f"`{input[0]}`라는 명령어는 존재하지 않습니다.")
        elif len(input) > 1:
            embed = discord.Embed(title=":no_entry: **Error!**", description="구문이 너무 많습니다.")

        embed.set_footer(text=f"{ctx.author.name}{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        embed.color=self.embed_color
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))