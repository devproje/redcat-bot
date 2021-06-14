import discord, random, os, asyncio
from discord.ext import commands

def setup(bot):
    bot.add_cog(WinCho(bot))

def wincho_mention(mention_type):
    mention = "<@!602733713842896908>"
    if mention_type == 0:
        return f"{mention} 빨리 와바"
    elif mention_type == 1:
        return f"{mention} 빨리 안와?"
    elif mention_type == 2:
        return f"{mention} 야 윈초야 큰일났어 빨리 와봐!!"
    elif mention_type == 3:
        return f"{mention} 윈초 뭐해?"
    elif mention_type == 4:
        return f"{mention} 윈초 빼애애애애액"
    elif mention_type == 5:
        return f"{mention} 윈트초코 뭐해?"
    elif mention_type == 6:
        return f"{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}"

def get_image(image_type):
    if image_type == 0:
        return "https://ak.picdn.net/shutterstock/videos/1014557474/thumb/1.jpg"
    elif image_type == 1:
        return "https://d2culxnxbccemt.cloudfront.net/craft/content/uploads/2020/07/30221830/image-001.jpg"
    elif image_type == 2:
        return "http://netherald.kro.kr:8080/apps/files_sharing/publicpreview/DSmMZADoMxB2kGM?x=1457&y=383&a=true&file=Burnt_Wintchoco.jpg&scalingup=0"
    else:
        return None

class WinCho(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0xFFF1D6

        self.author_id = 415801068174180352

    @commands.command(name="wincho")
    async def wincho(self, ctx, wincho_action=None):
        if wincho_action == "smash":
            embed = discord.Embed(description="**Smashing Wincho!**", color=self.embed_color)
            embed.set_image(url=get_image(1))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif wincho_action == "melt":
            embed = discord.Embed(description="**Melting Wincho!**", color=self.embed_color)
            embed.set_image(url=get_image(0))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif wincho_action == "call":
            if ctx.author.id != self.author_id:
                embed = discord.Embed(title=":no_entry: **Execute Error!**", description="**This command is only use bot owner!**", color=self.embed_color)
                await ctx.send(embed=embed)
            else:
                await ctx.channel.send(wincho_mention(random.randrange(0, 7)))
        elif wincho_action == "burn":
            embed = discord.Embed(description="**Burning Wincho!**", color=self.embed_color)
            embed.set_image(url=get_image(2))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif wincho_action is None:
            embed = discord.Embed(title=":question: Wincho help", description="`\\wincho` `<burn | smash | melt | call>`", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error!", description=f"{wincho_action} is not found!", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(name="윈초")
    async def wincho_korean(self, ctx, wincho_action=None):
        if wincho_action == "부수기":
            embed = discord.Embed(description="**윈초 부수기!**", color=self.embed_color)
            embed.set_image(url=get_image(1))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif wincho_action == "녹이기":
            embed = discord.Embed(description="**윈초 녹이기!**", color=self.embed_color)
            embed.set_image(url=get_image(0))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif wincho_action == "부르기":
            if ctx.author.id != self.author_id:
                embed = discord.Embed(title=":no_entry: Execute Error!", description="**This command is only use bot owner!**", color=self.embed_color)
                await ctx.send(embed=embed)
            else:
                await ctx.channel.send(wincho_mention(random.randrange(0, 7)))
        elif wincho_action == "태우기":
            embed = discord.Embed(description="**윈초 태우기!**", color=self.embed_color)
            embed.set_image(url=get_image(2))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif wincho_action is None:
            embed = discord.Embed(title=":question: 윈초 커맨드 도움말", description="`\\윈초` `<녹이기 | 부수기 | 녹이기 | 부르기>`", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=":no_entry: **오류발생!**", description=f"{wincho_action}은(는) 존재하지 않습니다!", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
