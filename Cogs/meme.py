import discord
from discord.ext import commands
from discord_slash import cog_ext

def setup(bot):
    bot.add_cog(Mime(bot))

def image_selector(number):
    if number == None:
        return None
    elif number == 1:
        return "https://media.discordapp.net/attachments/860725885703421954/860748785886298132/94d3b03465314b2f.gif"
    elif number == 2:
        return "https://media.discordapp.net/attachments/860725885703421954/860748791627907072/Nuclear.gif"
    elif number == 3:
        return "https://media.discordapp.net/attachments/860725885703421954/860748788979990568/boom.gif"
    elif number == 4:
        return "http://i.imgur.com/DHshyTY.gif"
    elif number == 5:
        return "https://media.discordapp.net/attachments/860725885703421954/860748778909728768/d5d301e01935b062.jpg?width=739&height=416"
    elif number == 6:
        return "https://media.discordapp.net/attachments/860725885703421954/860748781012516864/2.gif"
    elif number == 7:
        return "https://media.discordapp.net/attachments/860725885703421954/860748778951540746/3f2366b6cddfab25.gif?width=282&height=416"
    elif number == 8:
        return "https://media.discordapp.net/attachments/860725885703421954/860748785148100608/1902___795767943.gif"

class Mime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0xED4245

    @cog_ext.cog_slash(name="meme", description="You can use Project_TL's meme image!")
    async def _meme(self, ctx, argument=None):
        if argument is None:
            embed = discord.Embed(title=":no_entry: **에러발생**", description="구문은 공백이 될 수 없습니다.", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator} * Powered by Discord", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif argument == "정의의후폭풍":
            embed = discord.Embed(description="**:rocket: 정의의 후폭풍!**", color=self.embed_color)
            embed.set_image(url=image_selector(1))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator} * Powered by Discord", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif argument == "핵폭탄":
            embed = discord.Embed(description="**:boom: 핵 폭발!**", color=self.embed_color)
            embed.set_image(url=image_selector(2))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator} * Powered by Discord", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif argument == "극장폭파":
            embed = discord.Embed(description="**:boom: 극장 폭파**", color=self.embed_color)
            embed.set_image(url=image_selector(3))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator} * Powered by Discord", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif argument == "고자라니":
            embed = discord.Embed(description="**:no_entry: 심영짤**", color=self.embed_color)
            embed.set_image(url=image_selector(4))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator} * Powered by Discord", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif argument == "의사양반":
            embed = discord.Embed(description="**:no_entry: Aㅏ 안심하시오, 병원이오.**", color=self.embed_color)
            embed.set_image(url=image_selector(5))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator} * Powered by Discord", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif argument == "의사양반2":
            embed = discord.Embed(description="**:no_entry: Aㅏ 안심하시오, 병원이오.**", color=self.embed_color)
            embed.set_image(url=image_selector(6))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator} * Powered by Discord", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif argument == "섬광탄":
            embed = discord.Embed(description="**:no_entry: 눈뽕!**", color=self.embed_color)
            embed.set_image(url=image_selector(7))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator} * Powered by Discord", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif argument == "파괴":
            embed = discord.Embed(description="**:no_entry: 널 파괴한다..!**", color=self.embed_color)
            embed.set_image(url=image_selector(8))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator} * Powered by Discord", icon_url=ctx.author.avatar_url)
        else:
            embed = discord.Embed(title=":no_entry: **오류발생!**", description=f"{argument}은(는) 존재하지 않습니다!", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator} * Powered by Discord", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
