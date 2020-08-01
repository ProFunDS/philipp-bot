import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
import os
import random
import mylist

Phil = commands.Bot(command_prefix= "dl.")
Phil.remove_command('help')

@Phil.event
async def on_ready():
	print ('Всё заебись!')

@Phil.event
async def on_member_join(member):
	add_start_role = discord.utils.get(member.guild.roles, id = 730771639788371968)
	await member.add_roles(add_start_role)

@Phil.command(aliases = ['admins'])
async def admin(ctx):
	await ctx.send(f'**#4708 Эльдар** :fleur_de_lis: \n**#5665 Филя** <:morgana:722944166262472734> \n**#0641 Тёма** <:xayah:723194132209729566> \n**#1952 Даня** <:jinx:722932714977886298> \n**#6994 Аня** <:annya:736657198427537448> \n**#5158 Ералхан** <:draven_think:739115745832730696>')  

@Phil.command(pass_context=True)
async def choose(ctx, lane: str = None):
	author = ctx.message.author
	if lane is None:
		champion = random.choice(mylist.champions)
		motivation = random.choice(mylist.motivations)
		emoji = random.choice(mylist.emojis)
		emoj = random.choice(mylist.emojis)
		await ctx.message.delete()
		await ctx.send(f"{emoj} {author.mention}, попробуй **{champion}**{motivation} {emoji}")
	elif lane == 'top':
		tp = random.choice(mylist.top)
		emoji = random.choice(mylist.emojis)
		emoj = random.choice(mylist.emojis)
		await ctx.message.delete()
		await ctx.send(f'{emoji} {author.mention}, возьми **{tp}** {emoj}')
	elif lane == 'jungle':
		jg = random.choice(mylist.jungle)
		emoji = random.choice(mylist.emojis)
		emoj = random.choice(mylist.emojis)
		await ctx.message.delete()
		await ctx.send(f'{emoji} {author.mention}, возьми **{jg}** {emoj}')
	elif lane == 'mid':
		md = random.choice(mylist.mid)
		emoji = random.choice(mylist.emojis)
		emoj = random.choice(mylist.emojis)
		await ctx.message.delete()
		await ctx.send(f'{emoji} {author.mention}, возьми **{md}** {emoj}')
	elif lane == 'bot':
		bt = random.choice(mylist.bot)
		emoji = random.choice(mylist.emojis)
		emoj = random.choice(mylist.emojis)
		await ctx.message.delete()
		await ctx.send(f'{emoji} {author.mention}, возьми **{bt}** {emoj}')
	elif lane == 'sup' or lane == 'support':
		sp = random.choice(mylist.support)
		emoji = random.choice(mylist.emojis)
		emoj = random.choice(mylist.emojis)
		await ctx.message.delete()
		await ctx.send(f'{emoji} {author.mention}, возьми **{sp}** {emoj}')
	else:
		await ctx.message.delete()
		await ctx.send(f'**{author.mention}, неверно указана линия.** \n **```(top | jungle | mid | bot | support)```**')

@Phil.command(pass_context=True) 
async def help(ctx):
	author = ctx.message.author
	await ctx.send(f"Никто тебе не поможет, {author.mention} :axe:")

@Phil.command(pass_context=True)
async def random_nick(ctx):
    first = random.choice(mylist.first_half)
    second = random.choice(mylist.second_half)
    await ctx.message.delete()
    await ctx.message.author.edit(nick=(first) + " " + (second))
    await ctx.send(f'**<:fiora:723182306432647270> Ваш никнейм успешно изменён, {ctx.message.author.mention}**')

token = os.environ.get('BOT_TOKEN')
Phil.run(str(token))
