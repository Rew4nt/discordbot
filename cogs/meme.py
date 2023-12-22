import MemeFactory
import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import asyncio


async def no_meme_name(ctx, meme_name):
    if meme_name is None or meme_name == "":
        await ctx.send(MemeFactory.if_no_meme)


class MemeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = None

    @commands.command()
    async def get_channel_id(self, ctx, channel: discord.TextChannel):
        self.channel_id = channel.id
        self.send_daily_meme.start()
        await ctx.send(f"The ID of the {channel.mention} channel is {channel.id}.")

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as {0.user}'.format(self.bot))

    @commands.command()
    async def generateMeme(self, ctx, meme_name: str = None, *args,):
        await no_meme_name(ctx, meme_name)
        meme_url = MemeFactory.generate_meme(meme_name, *args)
        await ctx.send(meme_url)

    @commands.command()
    async def displayTemplates(self, ctx):
        if not hasattr(self.bot, 'template_index'):
            self.bot.template_index = 0
        start = self.bot.template_index
        end = start + 10
        templates = MemeFactory.display_names(start, end)
        await ctx.send('\n'.join(templates))
        self.bot.template_index = end

    @commands.command()
    async def exampleMeme(self, ctx, meme_name: str = None):
        await no_meme_name(ctx, meme_name)
        meme_url = MemeFactory.example_meme(meme_name)
        await ctx.send(meme_url)

    @commands.command()
    async def getMeme(self, ctx, genre=None, image_format=None):
        meme_url = MemeFactory.get_meme(genre, image_format)
        embed = discord.Embed(color=discord.Color.random())
        embed.set_image(url=meme_url)
        embed.set_footer(text=f"Meme sent by {ctx.author}")
        await ctx.channel.send(embed=embed)

    @tasks.loop(hours=24)
    async def send_daily_meme(self):
        channel = self.bot.get_channel(self.channel_id)
        meme_url = MemeFactory.get_meme()
        embed = discord.Embed(color=discord.Color.random())
        embed.set_image(url=meme_url)
        await channel.send(meme_url)

    @send_daily_meme.before_loop
    async def before_send_daily_meme(self):
        now = datetime.now()
        next_run_time = now.replace(hour=9, minute=40, second=0)
        if now > next_run_time:
            next_run_time += timedelta(days=1)
        time_until_next_run = (next_run_time - now).total_seconds()
        await asyncio.sleep(time_until_next_run)


async def setup(bot):
    await bot.add_cog(MemeCog(bot))


