import discord, os, psutil
from discord.ext import commands

def setup(bot):
    bot.add_cog(BotInfo(bot))
"""
class GetInstanceUsage():
    def __init__(self):
        pid = os.getpid()
        py = psutil.Process(pid)
        psutil.cpu_percent()

        self.cpu_usage = os.popen("ps aux | grep " + str(pid) + " | grep -v grep | awk '{print $3}'").read()
        self.memory_usage = round(py.memory_info()[0] /2.**30, 2)
    
    def cpu_status(self):
        return self.cpu_usage

    def memory_status(self):
        return self.memory_usage
"""

class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF
        self.host = "Hosting by ADP_Community"

    @commands.command(name="status")
    async def botinfo(self, ctx):
        # usage_class = GetInstanceUsage()
        embed=(discord.Embed(title="ProjectBot-remake Status", description=f"{self.host}", color=self.embed_color))
        embed.add_field(name="CPU Usage", value=f"__{psutil.cpu_percent()}__%", inline=True)
        embed.add_field(name="RAM Usage", value=f"__{psutil.virtual_memory().percent}__%", inline=True)

        await ctx.send(embed=embed)