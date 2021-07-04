import discord, os, psutil, platform
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from datetime import timedelta

bot = commands.Bot(command_prefix="\\", help_command=None, intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)

bot_version="v1.0.0"
embed_color = 0x75B8FF

author_name="Project_TL#9436"
contributers=["None"]

owner_id = 415801068174180352

token_path = "token.txt"
open_token = open(token_path, "r", encoding = "utf-8")
token = open_token.read().split()[0]

for filename in os.listdir("Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print("Logined for ProjectBot")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"ProjectBot {bot_version}"))

@slash.slash(name="version")
async def version(ctx: SlashContext):
    embed = (discord.Embed(title=":dart: **Version**", description="This is command list", color=embed_color)
        .add_field(name=f"**Version**", value=f"{bot_version}", inline=True)
        .add_field(name=f"**Author**", value=author_name, inline=True)
        .add_field(name=f"**Contributers**", value=contributers, inline=True)
    
        .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))
    await ctx.channel.send(embed=embed)

def get_uptime():
    with open("/proc/uptime", 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        t = timedelta(seconds = uptime_seconds)
        return ("{} D | {} H | {} M".format(t.days, t.seconds // 3600, (t.seconds // 60) % 60))

@slash.slash(name="status")
async def status(ctx: SlashContext):
    host = "Hosting by **ADP_Community**"
    embed=(discord.Embed(title=f"ProjectBot-remake {bot_version} Status", description=f"{host}", color=embed_color)
        .add_field(name="**CPU USAGE**", value=f"__{psutil.cpu_percent()}%__", inline=True)
        .add_field(name="**RAM USAGE**", value=f"__{psutil.virtual_memory().percent}%__", inline=True)
        .add_field(name="**AVAILABLE USAGE**", value=f"__{round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, 1)}%__", inline=True)

        .add_field(name="**UPTIME**", value=f"__{get_uptime()}__", inline=True)
        .add_field(name="**SYSTEM INFO**", value=f"__{platform.system()} | {platform.machine()}__", inline=True)
        .add_field(name="**PING**", value=f"__{round(bot.latency * 1000)}ms__", inline=True)

        .add_field(name="OWNER", value=author_name, inline=True)
        .add_field(name="CONTRIBUTERS", value=contributers, inline=True)
        .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))

    await ctx.send(embed=embed)

bot.run(token)