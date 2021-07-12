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
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"{bot_name} {bot_version}"))
    
    activity = [f"{bot_name} {bot_version}", f"Uptime: {get_uptime()}"]
    await activity_switcher(activity)

async def activity_switcher(games):
    await bot.wait_until_ready()

    while not bot.is_closed():
        for g in games:
            await bot.change_presence(activity = discord.Game(g))
            await asyncio.sleep(20)

@slash.slash(name="load", description="You can load command")
async def load(ctx: SlashContext, extension):
    if ctx.author.id != self.author_id:
        embed = discord.Embed(title=f":stop_sign: **Error!**", description=f"You can't loaded **{extension}**!\nBecause you're not bot owner!")
        await ctx.send(embed=embed)
    else:
        bot.load_extension(f"Cogs.{extension}")
        embed = discord.Embed(title=f":white_check_mark: **Done!**", description=f"**{extension}** has successful loaded!")
        embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        
        await ctx.send(embed=embed)


@slash.slash(name="unload", description="You can unload command")
async def unload(ctx: SlashContext, extension):
    if ctx.author.id != self.author_id:
        embed = discord.Embed(title=f":stop_sign: **Error!**", description=f"You can't unloaded **{extension}**!\nBecause you're not bot owner!")
        embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        
        await ctx.send(embed=embed)
    else:
        bot.unload_extension(f"Cogs.{extension}")
        embed = discord.Embed(title=f":white_check_mark: **Done!**", description=f"**{extension}** has successful unloaded!")
        embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        
        await ctx.send(embed=embed)

@slash.slash(name="reload")
async def reload_commands(ctx: SlashContext, extension=None):
    await ctx.defer()
    reboot_embed_color = 0xED4245

    if ctx.author.id == owner_id:
        if extension is None:
            for filename in os.listdir("Cogs"):
                if filename.endswith(".py"):
                    bot.unload_extension(f"Cogs.{filename[:-3]}")
                    bot.load_extension(f"Cogs.{filename[:-3]}")

            embed = discord.Embed(name=":white_check_mark: Done!", description="All command is reloaded!", color=reboot_embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        
        else:
            bot.unload_extension(f"Cogs.{extension}")
            bot.load_extension(f"Cogs.{extension}")
            
            embed = discord.Embed(name=":white_check_mark: Done!", description=f"{extension} is reloaded!", color=reboot_embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            
            await ctx.send(embed=embed)
    
    else:
        embed = discord.Embed(name=":stop_sign: Error", description="You're not bot owner!", color=reboot_embed_color)
        embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        
        await ctx.send(embed=embed)

host = f"Hosting by **{host_name}**"

@slash.slash(name="botinfo", description="You can show bot info.")
async def version(ctx: SlashContext):
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
    await ctx.send(embed=embed)

def get_uptime():
    with open("/proc/uptime", 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        t = timedelta(seconds = uptime_seconds)
        return ("{} D | {} H | {} M".format(t.days, t.seconds // 3600, (t.seconds // 60) % 60))

@slash.slash(name="status")
async def status(ctx: SlashContext):
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

@slash.slash(name="version")
async def version(ctx: SlashContext):
    await ctx.send(f"My version is {bot_version}")

bot.run(token)
