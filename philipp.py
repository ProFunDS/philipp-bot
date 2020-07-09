import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

Phil = commands.Bot(command_prefix= "!")

@Phil.event
async def on_member_join(member):
	add_start_role = discord.utils.get(member.guild.roles, id = 730771639788371968)
	await member.add_roles(add_start_role)

@Phil.event
async def on_ready():
	print ('Всё заебись!')

@Phil.command(pass_context=True) 
async def change(ctx):
	author = ctx.message.author
	await ctx.send(f"Чё ты хочешь {author.mention}? Заебал")

token = os.environ.get('BOT_TOKEN')