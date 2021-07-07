import discord
from discord.ext import commands
from discord_slash import SlashContext, cog_ext

def setup(bot):
    bot.add_cog(PingPong(bot))

class PingPong(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0xED4245

    @commands.command(name="ping")
    async def ping(self, ctx):
        embed = discord.Embed(title=":ping_pong: Pong!", description=f"{round(self.bot.latency * 1000)}ms", color=self.embed_color)
        embed.set_footer(text=f"{ctx.author.name}{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        
        await ctx.send(embed=embed)

    @commands.command(name="pong")
    async def pong(self, ctx):
        embed=discord.Embed(title=":ping_pong: Ping!", description=f"{round(self.bot.latency * 1000)}ms", color=self.embed_color)
        embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="ping", description="You can ping pong with bot")
    async def ping(self, ctx: SlashContext):
        embed = discord.Embed(title=":ping_pong: Pong!", description=f"{round(self.bot.latency * 1000)}ms", color=self.embed_color)
        embed.set_footer(text=f"{ctx.author.name}{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="pong", description="You can ping pong with bot")
    async def pong(self, ctx: SlashContext):
        embed=discord.Embed(title=":ping_pong: Ping!", description=f"{round(self.bot.latency * 1000)}ms", color=self.embed_color)
        embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        
        await ctx.send(embed=embed)