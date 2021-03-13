import os
from discord.ext import commands
from config import owner


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_ctx=True, brief="Delete a sound.",
                      description=f"Delete a file from sounds. Only usable by owner. ({owner})")
    async def delete(self, ctx, *name):
        if str(ctx.author) == owner:
            directory = os.listdir("sounds")
            for file in directory:
                if file == name[0] + ".mp3":
                    os.remove("sounds/" + file)
                    await ctx.send(f"{file[:-4]} was removed successfully.")
        else:
            await ctx.send(f"You have no power here. I listen only to my owner. {owner}")

    @commands.command(pass_ctx=True, brief="For debugging.",
                      description=f"For debugging a specific command. Only usable by owner. ({owner})")
    async def debug(self, ctx):
        if str(ctx.author) == owner:
            pass
            

def setup(bot):
    bot.add_cog(Owner(bot))
