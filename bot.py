import discord, os, psutil, platform, asyncio, platform
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from datetime import timedelta, datetime

bot = commands.Bot(command_prefix="\\", help_command=None, intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)

bot_name="RedCat"
bot_version="v1.0.0"

author_name="Project_TL#9436"
contributers=["None"]

embed_color = 0xED4245
owner_id = 415801068174180352

host_name="ADP_Community"

maintance_file="maintance.txt"
open_maintance=open(maintance_file, "r", encoding="utf-8")
maintance=open_maintance.read().split[0]

token_path = "token.txt"
open_token = open(token_path, "r", encoding = "utf-8")
token = open_token.read().split()[0]

for filename in os.listdir("Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")

now = datetime.now()


@bot.event
async def on_ready():
    print(f"Logined for {bot_name}")
    activity = [f"{bot_name} {bot_version}", f"Uptime: {get_uptime()}"]

    if maintance == "true":
        with open(f'profile_image/maintance/dark.png', 'rb') as profile_image:
            await bot.user.edit(avatar=profile_image.read())
        activity_switcher(activity)
    else:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"{bot_name} {bot_version}"))
        await activity_switcher(activity)

async def activity_switcher(activity):
    await bot.wait_until_ready()
    
    if not maintance == "true":
        while not bot.is_closed():
            for g in activity:
                await bot.change_presence(activity = discord.Game(g))
                await asyncio.sleep(20)
    else:
        maintance_activity = [f"{bot_name} is maintance", "⛔️ MAINTANCE"]
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(f"{bot_name} is maintance"))
        while not bot.is_closed():
            for act in maintance_activity:
                await bot.change_presence(activity = discord.Game(act))

host = f"Hosting by **{host_name}**"

async def run_bot_info(ctx):
    await ctx.defer()

    embed = (discord.Embed(title=f":dart: **{bot_name}** info", description=f"{host}", color=embed_color)
        .add_field(name="**Name**", value=f"{bot_name}")
        .add_field(name=f"**Version**", value=f"{bot_version}", inline=True)
        .add_field(name="**Type**", value="Opensource Bot", inline=True)
        .add_field(name=f"**Author**", value=f"{author_name}", inline=True)
        .add_field(name=f"**Contributers**", value=f"{contributers}", inline=True)
        .set_thumbnail(url=bot.user.avatar_url)
        .add_field(name="**Github**", value=f"[{bot_name} Github](https://github.com/ProjectTL12345/redcat-bot)", inline=True)

        .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))
    await ctx.channel.send(embed=embed)

@slash.slash(name="botinfo", description="You can show bot info.")
async def version(ctx: SlashContext):
    if maintance == "true":
        if ctx.author_id == owner_id:
            run_bot_info(ctx)
        else:
            return None

    else:
        run_bot_info(ctx)

def get_uptime():
    with open("/proc/uptime", 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        t = timedelta(seconds = uptime_seconds)
        return ("{} D | {} H | {} M".format(t.days, t.seconds // 3600, (t.seconds // 60) % 60))

async def run_status(ctx):
    embed=(discord.Embed(title=f"{bot_name} {bot_version} Status", description=f"{host}", color=embed_color)
        .add_field(name="**CPU USAGE**", value=f"__{psutil.cpu_percent()}%__", inline=True)
        .add_field(name="**RAM USAGE**", value=f"__{psutil.virtual_memory().percent}%__", inline=True)
        .add_field(name="**AVAILABLE USAGE**", value=f"__{round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, 1)}%__", inline=True)

        .add_field(name="**UPTIME**", value=f"__{get_uptime()}__", inline=True)
        .add_field(name="**SYSTEM INFO**", value=f"__{platform.system()} | {platform.machine()}__", inline=True)
        .add_field(name="**LATENCY**", value=f"__{round(bot.latency * 1000)}ms__", inline=True)
        
        .add_field(name="**PYTHON VER**", value=f"{platform.python_version()}")
        .add_field(name="**OWNER**", value=author_name, inline=True)
        .add_field(name="**CONTRIBUTERS**", value=contributers, inline=True)

        .set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url))

    await ctx.send(embed=embed)

@slash.slash(name="status")
async def status(ctx: SlashContext):
    if maintance == "true":
        if ctx.author_id == owner_id:
            run_status(ctx)
        else:
            return None
    else:
        run_status(ctx)

@slash.slash(name="version")
async def version(ctx: SlashContext):
    if maintance == "true":
        if ctx.author_id == owner_id:
            await ctx.send(f"My version is {bot_version}")
        else:
            return None
    else:
        await ctx.send(f"My version is {bot_version}")

bot.run(token)
