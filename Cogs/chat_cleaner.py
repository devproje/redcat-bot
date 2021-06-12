import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(ChatCleaner(bot))

class ChatCleaner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF

    @commands.command(name="clear")
    async def chat_cleaner(self, ctx, amount: int = None):
        if ctx.author.id == 415801068174180352:
            if amount > 1:
                await ctx.channel.purge(limit=amount)
                embed = discord.Embed(title=":white_check_mark: **Chat Removed**", description=f"{amount} chats is removed!", color=self.embed_color)
                embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
            elif amount == 1:
                await ctx.channel.purge(limit=amount)
                embed = discord.Embed(title=":white_check_mark: **Chat Removed**", description=f"{amount} chat is removed!", color=self.embed_color)
                embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
            elif amount > 300:
                embed = discord.Embed(title=":no_entry: **Error!**", description=f"**REASON:** {amount} chats is too much!", color=self.embed_color)
                embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title=f":no_entry: **Error!**", description=f"**REASON:** You're not manager or owner!", color=self.embed_color)
                embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)