import discord
from discord.ext import commands
from discord.ext.commands import bot_has_permissions, has_permissions



class Ping(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        bot_latency = round(self.client.latency*1000)

        await ctx.send(f"Bot latency **{bot_latency} ms**")

    

    

async def setup(client):
    await client.add_cog(Ping(client))


