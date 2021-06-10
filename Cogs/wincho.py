import discord, os, asyncio
from discord.ext import commands

def setup(bot):
    bot.add_cog(WinCho(bot))

class WinCho(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF

    @commands.command(name="wincho")
    async def wincho(self, ctx, wincho_action):
        if wincho_action == "smash":
            embed = discord.Embed(description="**윈초 부수기!**", color=self.embed_color)
            embed.set_image(url="https://d2culxnxbccemt.cloudfront.net/craft/content/uploads/2020/07/30221830/image-001.jpg")
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif wincho_action == "melt":
            embed = discord.Embed(description="**윈초 녹이기!**", color=self.embed_color)
            embed.set_image(url="https://ak.picdn.net/shutterstock/videos/1014557474/thumb/1.jpg")
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif wincho_action == "call":
            await ctx.channel.send("<@!602733713842896908> 빨리와바")

    @commands.command(name="윈초")
    async def wincho_korean(self, ctx, wincho_action):
        if wincho_action == "부수기":
            embed = discord.Embed(description="**윈초 부수기!**", color=self.embed_color)
            embed.set_image(url="https://d2culxnxbccemt.cloudfront.net/craft/content/uploads/2020/07/30221830/image-001.jpg")
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif wincho_action == "녹이기":
            embed = discord.Embed(description="**윈초 녹이기!**", color=self.embed_color)
            embed.set_image(url="https://ak.picdn.net/shutterstock/videos/1014557474/thumb/1.jpg")
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif wincho_action == "부르기":
            await ctx.channel.send("<@!602733713842896908> 빨리와바")

    @wincho.error
    async def choco_error(self, ctx, error):
        embed = discord.Embed(title="Error!", descroption=f"{error} is not found!", color=self.embed_color)
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @wincho_korean.error
    async def choco_error_korea(self, ctx, error):
        embed = discord.Embed(title="오류발생!", descroption=f"{error}가 존재하지 않습니다!", color=self.embed_color)
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)