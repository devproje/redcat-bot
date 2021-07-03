import discord
from discord.ext import commands
from discord_slash import SlashContext, cog_ext

def setup(bot):
    bot.add_cog(ChatCleaner(bot))

class ChatCleaner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF
        self.owner_id = 415801068174180352

    @commands.command(name="clear")
    async def chat_cleaner(self, ctx, amount: int = None):
        if ctx.author.id == self.owner_id or ctx.author.guild_permissions.administrator:
            if amount < 301 and amount > 0:
                embed = discord.Embed(title=":white_check_mark: **Chat Removed**", description=f"{amount} chats is removed!", color=self.embed_color)
                await ctx.channel.purge(limit=amount + 1)
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

    @cog_ext.cog_slash(name="clear", description="You can remove chat (Admin or bot owner only)")
    async def chat_cleaner(self, ctx: SlashContext, amount: int = None):
        if ctx.author.id == self.owner_id or ctx.author.guild_permissions.administrator:
            if amount < 301 and amount > 0:
                embed = discord.Embed(title=":white_check_mark: **Chat Removed**", description=f"{amount} chats is removed!", color=self.embed_color)
                await ctx.channel.purge(limit=amount)
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