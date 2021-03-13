import os
import time
import discord
from discord.ext import commands
from config import prefix


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_ctx=True, brief="Play a sound.",
                      description="Play a sound in the voice channel.")
    async def play(self, ctx, sound):
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = discord.FFmpegPCMAudio("sounds/" + sound + ".mp3")
            voice.play(source)
            while ctx.voice_client.is_playing():
                time.sleep(2)
            else:
                await ctx.voice_client.disconnect()

        else:
            await ctx.send("You are not in a voice channel.")

    @commands.command(pass_ctx=True, brief="List all sounds.",
                      description="Lists all currently available sounds.")
    async def playlist(self, ctx):
        directory = os.listdir("sounds")
        arr = ["Available Sounds", ""]
        for file in directory:
            file = file.split(".")[0]
            arr.append(file)

        arr = "\n".join(map(str, arr))
        await ctx.send("```" + arr + "```")

    @commands.command(pass_ctx=True, brief="Add a sound.",
                      description=f"Upload a .mp3 file with {prefix}add <name> in the upload comment.")
    async def add(self, ctx, *name):
        if ctx.message.attachments:
            if ctx.message.attachments[0].filename.endswith("mp3"):
                file_name = "sounds/"
                for file in name:
                    file_name += file + ""
                    if file_name.endswith(" "):
                        file_name = file_name[:-1]
                    file_name += ".mp3"
                    file_name = file_name.lower()

                    await ctx.message.attachments[0].save(file_name)
                    await ctx.send(f"Sound added to bot. Play it in a voice channel with {prefix}play {file_name[:-4]}")
            else:
                await ctx.send("That is not a valid mp3 file.")
        else:
            await ctx.send(f"No file found. Upload a mp3 file and type {prefix}add <name> in the file comment.")


def setup(bot):
    bot.add_cog(Commands(bot))
