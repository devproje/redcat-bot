import discord, random
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

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
        return "https://cdn.discordapp.com/attachments/860725885703421954/860748788998209536/Burnt_Wintchoco.jpg"
    elif image_type == 3:
        return "https://cdn.discordapp.com/attachments/860725885703421954/860748787142885376/11c8299c3b69583f.png"
    else:
        return None

class WinCho(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0xFFF1D6

        self.author_id = 415801068174180352

    @cog_ext.cog_slash(name="wincho", description="You can broken wintchoco")
    async def wincho(self, ctx: SlashContext, wincho_action):
        ctx.defer()
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
                await ctx.send(wincho_mention(random.randrange(0, 7)))
        elif wincho_action == "burn":
            embed = discord.Embed(description="**Burning Wincho!**", color=self.embed_color)
            embed.set_image(url=get_image(2))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif wincho_action == "프젝기술":
            embed = discord.Embed(description="**윈초야 이리와 녹여줄게!**", color=self.embed_color)
            embed.set_image(url=get_image(3))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif wincho_action is None:
            embed = discord.Embed(title=":no_entry: **Error!**", description="Subcommand is not be None", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=":no_entry: **Error!**", description=f"{wincho_action} is not found!", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="윈초", description="당신은 윈초를 괴롭힐 수 있습니다")
    async def wincho_korean(self, ctx: SlashContext, wincho_action):
        ctx.defer()
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
                await ctx.send(wincho_mention(random.randrange(0, 7)))
        elif wincho_action == "태우기":
            embed = discord.Embed(description="**윈초 태우기!**", color=self.embed_color)
            embed.set_image(url=get_image(2))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif wincho_action == "프젝기술":
            embed = discord.Embed(description="**윈초야 이리와 녹여줄게!**", color=self.embed_color)
            embed.set_image(url=get_image(3))
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif wincho_action is None:
            embed = discord.Embed(title=":no_entry: **오류발생!**", description="보조 커맨드는 공백일 수 없습니다!", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=":no_entry: **오류발생!**", description=f"{wincho_action}은(는) 존재하지 않습니다!", color=self.embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
