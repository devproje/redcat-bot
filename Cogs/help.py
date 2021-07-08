import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

def setup(bot):
    bot.add_cog(Help(bot))

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0xED4245
        self.author_id=415801068174180352

    @cog_ext.cog_slash(name="help", description="You can see commands list!")
    async def help(self, ctx: SlashContext, argument=None):
        await ctx.defer()
        helper=EmbedHelper()

        if argument == None:
            embed = (discord.Embed(title=":dart: **Help**", description="**This is command list**", color=self.embed_color)
                .add_field(name="**Slash Command**", value="Slash command help\n**This feature is beta!**", inline=False)
                .add_field(name="`/ping`", value="You can ping pong with bot", inline=True)
                .add_field(name="`/pong`", value="You can ping pong with bot", inline=True)
                .add_field(name="`/carrot`", value="Help! :carrot:", inline=True)
                .add_field(name="`/wincho <action>`", value="you can broken wintchoco", inline=True)
                .add_field(name="`/윈초 <action>`", value="당신은 윈초를 괴롭힐 수 있습니다", inline=True)
                .add_field(name="`/avatar <mention>`", value="You can grab target person's avatar image", inline=True)
                .add_field(name="`/botinfo`", value="You can see this bot version", inline=True)
                .add_field(name="`/clear <amount>`", value="You can remove chat **(Admin or bot owner only)**", inline=True)
                .add_field(name="`/status`", value="You can see instance status!", inline=True)
                .add_field(name="`/meme`", value="You can use Project_TL's meme image!", inline=True)
                .add_field(name="`/help <command>`", value="Open help embed", inline=True)
            
                .add_field(name="**Normal Command**", value="This is normal command help (prefix = `\\`)", inline=False))

            if ctx.author.id != self.author_id:
                embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            else:
                embed.add_field(name="**Bot owner command**", value="This command only can use with bot owner", inline=False)
                embed.add_field(name="`/reboot`", value="Reboot command\n**Update bot only**", inline=True)
                embed.add_field(name="`/reload <None or extention>`", value="Reload command", inline=True)
                embed.add_field(name="`/notice <text>`", value="notice command", inline=True)
                embed.add_field(name="`/load <extension_name>`", value="You can load command", inline=True)
                embed.add_field(name="`/unload <extension_name>`", value="You can unload command", inline=True)
                embed.add_field(name="`/push`", value="You can push instance code", inline=True)
                embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)

            await ctx.channel.send(embed=embed)
        
        elif argument == "music":
            await ctx.send(embed=helper.help_music(ctx, self.embed_color))

        elif argument == "ping":
            await ctx.send(embed=helper.ping_pong(ctx, self.embed_color, False))

        elif argument == "pong":
            await ctx.send(embed=helper.ping_pong(ctx, self.embed_color, True))

        elif argument == "carrot":
            await ctx.send(embed=helper.carrot(ctx, self.embed_color))
        
        elif argument == "wincho":
            await ctx.send(embed=helper.wincho(ctx, self.embed_color, False))

        elif argument == "윈초":
            await ctx.send(embed=helper.wincho(ctx, self.embed_color, True))
        
        elif argument == "avatar":
            await ctx.send(embed=helper.avatar(ctx, self.embed_color))

        elif argument == "botinfo":
            await ctx.send(embed=helper.botinfo(ctx, self.embed_color))

        elif argument == "clear":
            await ctx.send(embed=helper.clear(ctx, self.embed_color))

        elif argument == "status":
            await ctx.send(embed=helper.status(ctx, self.embed_color))

        else:
            embed = (discord.Embed(title=":no_entry_sign: **Error!**", description=f"**{argument}** is not exist", color=self.embed_color))
            await ctx.channel.send(embed=embed)

class EmbedHelper():
    def help_music(self, ctx, embed_color):
        embed = (discord.Embed(title=":musical_note: **Music Help**", description="This is music options!", color=embed_color)
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
            .add_field(name="`\\leave`", value="Leave bot", inline=True)
            .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))

        return embed
    
    def ping_pong(self, ctx, embed_color, pong):
        if pong == False:
            embed = (discord.Embed(title=":ping_pong: **Ping Help**", description="If you type `/ping`, bot will respond with pong!", color=embed_color)
                .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))
            return embed

        else:
            embed = (discord.Embed(title=":ping_pong: **Pong Help**", description="If you type `/pong`, bot will respond with ping!", color=embed_color)
                .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))
            return embed

    def carrot(self, ctx, embed_color):
        embed = (discord.Embed(title=":carrot: **Carrot Help**", description="If you type `/carrot`, Bot will throw carrot.", color=embed_color)
            .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))
        return embed
        
    def wincho(self, ctx, embed_color, korean):
        if not korean == True:
            embed = (discord.Embed(title=":question: **Wincho Help**", description="`/wincho` `<burn | smash | melt | call | 프젝기술>`", color=0xFFF1D6)
            .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))

            return embed
        else:
            embed = (discord.Embed(title=":question: **윈초 커맨드 도움말**", description="`/윈초` `<녹이기 | 부수기 | 녹이기 | 부르기 | 프젝기술>`", color=0xFFF1D6)
            .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))
            
            return embed

    def avatar(self, ctx, embed_color):
        embed = (discord.Embed(title=":frame_photo: **Avatar Help**", description="If you want use this, please mention person!\n`(Notification is not sented with mention person)`", color=self.embed_color)
        .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))
       
        return embed

    def botinfo(self, ctx, embed_color):
        embed = (discord.Embed(title=":question: **Botinfo Help**", description="If you wanna bot's informations, please type `/botinfo`", color=embed_color)
        .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))

        return embed
    
    def clear(self, ctx, embed_color):
        embed = (discord.Embed(title=":question: **Clear Help**", description="You can clear chat! (MAX: 300, MIN: 1)\nEx) `/clear Integer`")
        .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))

        return embed
    
    def status(self, ctx, embed_color):
        embed = (discord.Embed(title=":question: **Status Help**", description="If you wanna see remote hosting status, please type `/status`")
        .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))

        return embed