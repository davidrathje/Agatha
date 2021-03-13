import os
import discord
from discord.ext import commands
from config import prefix, token

client = commands.Bot(command_prefix=prefix)


@client.event
async def on_ready():
    print()
    print("     _______               ___________             _______________   ")
    print("     ___    |______ ______ __  /___  /_______ _    ___    |___  _/   ")
    print("     __  /| |_  __ `/  __ `/  __/_  __ \  __ `/    __  /| |__  /     ")
    print("     _  ___ |  /_/ // /_/ // /_ _  / / / /_/ /     _  ___ |_/ /      ")
    print("     /_/  |_|\__, / \__,_/ \__/ /_/ /_/\__,_/      /_/  |_/___/      ")
    print("            /____/                                                   ")
    print("                                 - The world is your oyster        \n")

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=prefix+"help"))

    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            try:
                client.load_extension(f"cogs.{file[:-3]}")
                print("     Loaded", file[:-3].capitalize().replace("_", " "))
            except Exception as error:
                print(error)

client.run(token)
