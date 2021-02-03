import discord
from discord.ext import commands
import random

bot_prefix = '.'

TOKEN = "YOUR TOKEN"

print("YAY")

client = commands.Bot(command_prefix=bot_prefix, help_command=None)



@client.command()
async def nswf(ctx):
	sayi = random.randint(100,900)
	embed=discord.Embed(color=0xff0000)
	embed.set_image(url="http://porngif.it/gif/ze%20predu/0" + str(sayi) + ".gif")
	await ctx.send(embed=embed)
    
    
client.run(TOKEN) 
