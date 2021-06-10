import discord, os, asyncio
from discord.ext import commands

def setup(bot):
    bot.add_cog(bot)

class WintChoco(commands.Cog):
    async def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF

    @commands.command("wintchoco")
    async def wint_choco(self, ctx, action):
        if action == "smash":
            embed = discord.Embed(description="**윈초 부수기!**", color=self.embed_color)
            embed.set_image(url="https://d2culxnxbccemt.cloudfront.net/craft/content/uploads/2020/07/30221830/image-001.jpg")
            await ctx.send(embed=embed)
        elif action == "melt":
            embed = discord.Embed(description="**윈초 녹이기!**", color=self.embed_color)
            embed.set_image(url="https://ak.picdn.net/shutterstock/videos/1014557474/thumb/1.jpg")
            await ctx.send(embed=embed)
        else:
            return None

    @wint_choco.error
    async def on_error(self, ctx, error):
        embed = discord.Embed(title="Error!", descroption=f"{error} is not found!", color=self.embed_color)
        await ctx.send(embed=embed)