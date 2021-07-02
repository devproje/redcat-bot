import discord, os, asyncio, psutil, platform
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext
from discord_slash.utils.manage_commands import create_option
from datetime import timedelta
from discord.ext import commands

token_path = "token.txt"
open_token = open(token_path, "r", encoding = "utf-8")
token = open_token.read().split()[0]

bot_version="v0.9.0"
embed_color = 0x75B8FF

bot = commands.Bot(command_prefix="/", help_command=None)
owner_id = 415801068174180352

slash = SlashCommand(bot, auto_register=True, override_type = True, sync_on_cog_reload=True)

for filename in os.listdir("Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print("Logined for ProjectBot")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"ProjectBot {bot_version}"))

@bot.command(name="version")
async def version(ctx):
    embed = discord.Embed(title=":dart: **Version**", description="This is command list", color=embed_color)
    embed.add_field(name=f"**Version**", value=f"{bot_version}", inline=True)
    embed.add_field(name=f"**Author**", value="Project_TL#9436", inline=True)
    embed.add_field(name=f"**Contributers**", value="None", inline=True)
    
    embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    await ctx.channel.send(embed=embed)

@bot.command(name="reload")
async def reload_commands(ctx, extension=None):
    if ctx.author.id == owner_id:
        if extension is None:
            for filename in os.listdir("Cogs"):
                if filename.endswith(".py"):
                    bot.unload_extension(f"Cogs.{filename[:-3]}")
                    bot.load_extension(f"Cogs.{filename[:-3]}")

            embed = discord.Embed(name=":white_check_mark: Done!", description="All command is reloaded!", color=embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)
        else:
            bot.unload_extension(f"Cogs.{extension}")
            bot.load_extension(f"Cogs.{extension}")
            embed = discord.Embed(name=":white_check_mark: Done!", description=f"{extension} is reloaded!", color=embed_color)
            embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(name=":stop_sign: Error", description="You're not bot owner!", color=embed_color)
        embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

def get_uptime():
    with open("/proc/uptime", 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        t = timedelta(seconds = uptime_seconds)
        return ("{} D | {} H | {} M".format(t.days, t.seconds // 3600, (t.seconds // 60) % 60))

status_options = [
    {
        "type" : 4,
        "data" : {
            "content" : "You can see instance status!"
        }
    }
]

@slash.slash(name="status", options=status_options)
async def status(ctx):
    host = "Hosting by **ADP_Community**"
    embed=(discord.Embed(title=f"ProjectBot-remake {bot_version} Status", description=f"{host}", color=embed_color))
    embed.add_field(name="**CPU USAGE**", value=f"__{psutil.cpu_percent()}%__", inline=True)
    embed.add_field(name="**RAM USAGE**", value=f"__{psutil.virtual_memory().percent}%__", inline=True)
    embed.add_field(name="**AVAILABLE USAGE**", value=f"__{round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, 1)}%__", inline=True)

    embed.add_field(name="**UPTIME**", value=f"__{get_uptime()}__", inline=True)
    embed.add_field(name="**SYSTEM INFO**", value=f"__{platform.system()} | {platform.machine()}__", inline=True)
    embed.add_field(name="**PING**", value=f"__{round(bot.latency * 1000)}ms__", inline=True)

    embed.add_field(name="OWNER", value=f"Project_TL#9436", inline=True)
    embed.add_field(name="CONTRIBUTERS", value="None", inline=True)
    embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)

    await ctx.send(content="status", embed=embed)
    
bot.run(token)