import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(Help(bot))

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF
        self.author_id=415801068174180352

    @commands.command(name="help")
    async def help(self, ctx, argument=None):
        if argument == "music":
            embed = (discord.Embed(title="**Music Help**", description="This is music options!", color=self.embed_color)
                .add_field(name="`\\play <url or name>`", value="Play music", inline=True)
                .add_field(name="`\\pause`", value="Pause music", inline=True)
                .add_field(name="`\\resume`", value="Resume music", inline=True)
                .add_field(name="`\\now`", value="Checking playing music", inline=True)
                .add_field(name="`\\queue`", value="Checking play list", inline=True)
                .add_field(name="`\\stop`", value="Stop all music", inline=True)
                .add_field(name="`\\skip`", value="Skip current music", inline=True)
                .add_field(name="`\\shuffle`", value="Shuffle current queue", inline=True)
                .add_field(name="`\\loop`", value="Loop current music", inline=True)
                .add_field(name="`\\remove <array_number>`", value="Remove queued target music", inline=True)
                .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))
            await ctx.send(embed=embed)
            
        elif argument == None:
            embed = (discord.Embed(title=":dart: **Help**", description="**This is command list**", color=self.embed_color)
                .add_field(name="**Slash Command**", value="Slash command help\nThis feature is beta!", inline=False)
                .add_field(name="`/ping`", value="You can ping pong with bot", inline=True)
                .add_field(name="`/pong`", value="You can ping pong with bot", inline=True)
                .add_field(name="`/carrot`", value="Help! :carrot:", inline=True)
                .add_field(name="`/wincho <action>`", value="you can broken wintchoco", inline=True)
                .add_field(name="`/윈초 <action>`", value="당신은 윈초를 괴롭힐 수 있습니다", inline=True)
                .add_field(name="`/profile <mention>`", value="You can grab target person's avatar image", inline=True)
                .add_field(name="`/version`", value="You can see this bot version", inline=True)
                .add_field(name="`/clear <amount>`", value="You can remove chat **(Admin or bot owner only)**", inline=True)
                .add_field(name="`/status`", value="You can see instance status!", inline=True)
            
                .add_field(name="**Normal Command**", value="This is normal command help (prefix \"\\\")", inline=False)
                .add_field(name="`\\help`", value="Open help embed", inline=True)
                .add_field(name="`\\music help`", value="You can see music command options!", inline=True)
                .add_field(name="`\\meme`", value="You can use Project_TL's meme image!", inline=True))

            if ctx.author.id != self.author_id:
                embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            else:
                embed.add_field(name="**Bot owner command**", value="This command only can use with bot owner", inline=False)
                embed.add_field(name="`/reboot`", value="Reboot command\n**Update bot only**", inline=True)
                embed.add_field(name="`/reload <None or extention>`", value="Reload command", inline=True)
                embed.add_field(name="`/notice <text>`", value="notice command", inline=True)
                embed.add_field(name="`/load <extension_name>`", value="You can load command", inline=True)
                embed.add_field(name="`/unload <extension_name>`", value="You can unload command", inline=True)
                embed.add_field(name="`\\push`", value="You can push instance code", inline=True)
                embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)

            await ctx.channel.send(embed=embed)

        else:
            embed = (discord.Embed(title=":no_entry_sign: **Error!**", description=f"**{argument}** is not exist", color=self.embed_color))
            await ctx.channel.send(embed=embed)
        
        