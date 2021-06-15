import discord, asyncio
from discord.ext import commands

def setup(bot):
    bot.add_cog(Mime(bot))

def image_selector(number):
    if number == None:
        return None
    elif number == 1:
        return "http://projecttl.net:8080/s/YZT8jk8GTgk7gb5/download/%EC%A0%95%EC%9D%98%EC%9D%98%20%ED%9B%84%ED%8F%AD%ED%92%8D.gif"
    elif number == 2:
        return "http://projecttl.net:8080/s/T3e9ZCzBBzGgy4H/download/Nuclear.gif"
    elif number == 3:
        return "http://projecttl.net:8080/s/aJCjtazJYWJpBo8/download/boom.gif"

class Mime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF

    @commands.command(name="meme")
    async def _meme(self, ctx, argument=None):
        if argument is None:
            embed = discord.Embed(title=":question: 밈 도움말", description="`\\meme` `<정의의후폭풍 | 핵폭탄 | 극장폭파>`", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif argument == "정의의후폭풍":
            embed = discord.Embed(description="**:rocket: 정의의 후폭풍!**", color=self.embed_color)
            embed.set_image(url=image_selector(1))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif argument == "핵폭탄":
            embed = discord.Embed(description="**:boom: 핵 폭발!**", color=self.embed_color)
            embed.set_image(url=image_selector(2))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif argument == "극장폭파":
            embed = discord.Embed(description="**:boom: 극장 폭파**", color=self.embed_color)
            embed.set_image(url=image_selector(3))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=":no_entry: **오류발생!**", description=f"{argument}은(는) 존재하지 않습니다!", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)