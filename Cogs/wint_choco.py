import discord, os, asyncio
from discord.ext import commands

def setup(bot):
    bot.add_cog(WintChoco(bot))

class WintChoco(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF

    @commands.command(name="wintchoco")
    async def wint_choco(self, ctx, wincho_action):
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

    @wint_choco.error
    async def choco_error(self, ctx, error):
        embed = discord.Embed(title="Error!", descroption=f"{error} is not found!", color=self.embed_color)
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)