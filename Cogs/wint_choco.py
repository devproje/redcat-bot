import discord, os, asyncio
from discord.ext import commands

def setup(bot):
    bot.add_cog(bot)

class WintChoco(commands.Cog):
    async def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF

    @commands.command(name="wintchoco")
    async def wint_choco(self, ctx, wincho_action):
        if wincho_action == "smash":
            embed = discord.Embed(description="**윈초 부수기!**", color=self.embed_color)
            embed.set_image(url="https://d2culxnxbccemt.cloudfront.net/craft/content/uploads/2020/07/30221830/image-001.jpg")
            await ctx.send(embed=embed)
        elif wincho_action == "melt":
            embed = discord.Embed(description="**윈초 녹이기!**", color=self.embed_color)
            embed.set_image(url="https://ak.picdn.net/shutterstock/videos/1014557474/thumb/1.jpg")
            await ctx.send(embed=embed)
        else:
            if wincho_action == None:
                embed = discord.Embed(title=":: Error!", descroption=f"You must type argument!", color=self.embed_color)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Error!", descroption=f"{wincho_action} is not found!", color=self.embed_color)
                await ctx.send(embed=embed)
        