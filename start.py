import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv('.env')
#bot = commands.Bot(command_prefix=config.PREFIX["command"], intents=discord.Intents().all())
bot = commands.Bot(command_prefix=os.getenv("PREFIX"), intents = discord.Intents().all())

@bot.event
async def on_ready():
    print('{0.user}'.format(bot), 'is ready')
    print("==================")
    await bot.change_presence(activity=discord.Game(name="Thanos Glove"))

@bot.event
async def on_message(message):  
    await bot.process_commands(message) 

@bot.command()
@commands.has_guild_permissions(administrator=True)
async def snap(ctx):
    try:
        print('Working...')
        file = discord.File("image/Thanos.gif")
        await ctx.channel.send(file = file)
        for members in ctx.author.voice.channel.members:    
            await members.move_to(None)
            embed = discord.Embed(description=f'@{members} was slain by Thanos, for the good of the Universe.')
            await ctx.send(embed=embed)
    except:
        embed = discord.Embed(description="Something Error.")
        await ctx.send(embed=embed)

bot.run(os.getenv("TOKEN"))