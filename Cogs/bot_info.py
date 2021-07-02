import discord, os, psutil
from discord.ext import commands

def setup(bot):
    bot.add_cog(BotInfo(bot))

class GetInstanceUsage():
    def __init__(self):
        pid = os.getpid()
        py = psutil.Process(pid)

        self.cpu_usage = os.popen("ps aux | grep " + str(pid) + " | grep -v grep | awk '{print $3}'").read()
        self.memory_usage = round(py.memory_info()[0] /2.**30, 2)
    
    def cpu_status(self):
        return self.cpu_usage

    def memory_status(self):
        return self.memory_usage
        

class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF
        self.host = "Hosting by ADP_Community"

    @commands.command(name="botinfo")
    async def botinfo(self, ctx):
        usage_class = GetInstanceUsage()
        embed=(discord.Embed(title="", description=f"{self.host}", color=self.embed_color)
            .add_field(name="CPU", value=f"{usage_class.cpu_status()}", inline=True)
            .add_field(name="Memory", value=f"{usage_class.memory_status()}", inline=True))
        await ctx.send(embed)