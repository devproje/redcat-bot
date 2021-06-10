import discord
from discord.ext import commands

def check_user(name, id):
    if name == "Project_TL" & id != "852387809481195520":
        return False
    else:
        return True