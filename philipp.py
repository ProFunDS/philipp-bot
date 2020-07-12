  
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import random

Phil = commands.Bot(command_prefix= "dl.")
Phil.remove_command('help')

champions = ['Азира', 'Акали', 'Алистара', 'Амуму', 'Анивию', 'Ари', 'Атрокса', 'Аурелион Сола', "Афелия",
	"Барда", "Блицранка", "Браума", "Брэнда", "Вай", "Варвика :wolf: ", "Варуса", "Вейгара", "Вейн", "Вел'Коза", 
	"Владимира", "Волибира", "Вуконга", "Галио", "Гангпланка", "Гарена", "Гекарима :horse_racing_tone1:", "Гнара", 
	"Грагаса", "Грейвза", "Дариуса", "Джакса", "Джарвана", "Джейса", "Джина", "Джинкс", "Диану", "Доктора Мундо", 
	"Дрейвена", "Жанну", "Зайру", "Зака", "Зеда", "Зерата", "Зиггса", "Зилеана", "Зои", "Иверна", "Иллаой", "Ирелию", 
	"Йорика", "Ка'Зикса", "Каина", "Кай'Су", "Калисту", "Камиллу", "Карму", "Картуса", "Кассадина", "Кассиопею", "Катарину", 
	"Квинн", "Кейл", "Кейтлин", "Кеннена", "Киану", "Киндред", "Кледа", "Ког'Мао", "Корки", "Ксин Жао", "Ле Блан", "Леону", 
	"Ли Сина", "Лиссандру", "Лулу", "Люкс", "Люциана", "Мальзахара", "Мальфита", "Маокая", "Мастера Йи", "Мисс Фортуну", 
	"Моргану", "Мордекайзера", "Нами", "Насуса", "Наутилуса", "Нидали :tiger:", "Нико :lizard:", "Ноктюрна", "Нуну и Виллумпа", 
	"Орианну :robot: ", "Орна", "Пайка", "Пантеона", "Поппи", "Райза", "Рамбла", "Раммуса", "Рек'Сай", "Ренгара", "Ренектона", 
	"Ривен", "Рэйкана", "Сайласа", "Свейна", "Седжуани", "Сенну", "Сетта", "Сивир", "Синджеда", "Синдру", "Сиона", "Скарнера", 
	"Сону", "Сораку", "Таам Кенча", "Талию", "Талона", "Тарика", "Твистед Фэйта", "Твича", "Тимо :japanese_ogre:", "Трандла", 
	"Треша", "Триндамира", "Тристану", "Удира", "Ургота", "Фиддлстикса", "Физза", "Фиору :person_fencing:", "Хеймердингера", 
	"Чо'Гата", "Шако", "Шаю", "Шена", "Шивану", "Эвелинн", "Эзреаля", "Экко", "Элизу", "Энни :fire:", "Эш", "Юми :smirk_cat:", 
	"Ясуо :man_in_manual_wheelchair_tone1:", "Лиллию", 'Олафа', "Виктора"]
top = ["Акали", "Атрокса", "Вейн", "Владимира", "Волибира", "Вуконга", "Гангпланка", "Гарена", "Гнара", "Дариуса", "Джакса", 
	"Джейса", "Доктора Мундо", "Иллаой", "Ирелию", "Йорика", "Камиллу", "Квинн", "Кейл", "Кеннена", "Кледа", "Мальфита", "Маокая",
	"Мордекайзера", "Насуса", "Орна", "Поппи", "Рамбла", "Ренектона", "Ривен", "Сайласа", "Сетта", "Синджеда", "Сиона", "Тимо",
	"Триндамира", "Ургота", "Фиору", "Чо'Гата", "Шена", "Ясуо"]
jungle = ["Амуму", "Вай", "Варвика", "Волибира", "Вуконга", "Гекарима", "Грагаса", "Грейвза", "Джакса", "Джарвана", "Зака", "Иверна",
	"Ка'Зикса", "Каина", "Картуса", "Киндред", "Ксин Жао", "Ли Сина", "Мастера Йи", "Нидали", "Ноктюрна", "Нуну и Виллумпа", "Олафа",
	"Раммуса", "Рек'Сай", "Ренгара", "Сайласа", "Седжуани", "Сетта", "Скарнера", "Талию", "Трандла", "Удира", "Фиддлстика", "Шако",
	"Шивану", "Эвелинн", "Экко", "Элизу"]
mid = ["Азира", "Акали", "Анивию", "Ари", "Аурелион Сола", "Вейгара", "Вел'Коза", "Виктора", "Владимира", "Галио", "Диану", "Зеда",
	"Зерата", "Зиггса", "Зои", "Ирелию", "Кассадина", "Кассиопею", "Катарину", "Киану", "Корки", "Ле Блан", "Лиссандру", "Люкс",
	"Мальзахара", "Нико", "Орианну", "Пантеона", "Райза", "Рамбла", "Сайласа", "Синдру", "Талона", "Твистед Фэйта", "Физза",
	"Хеймердингера", "Экко", "Энни", "Ясуо"]
bot = ["Афелия"," Варуса", "Вейна", "Джина", "Джинкс", "Дрейвена", "Кай'Су", "Калисту", "Кейтлин", "Ког'Мао", "Люциан", "Мисс Фортуну",
	"Сивир", "Твича", "Тристану", "Шаю", "Эзреаля", "Эш", "Ясуо"]
support = ["Алистара", "Барда", "Блицранка", "Браума", "Брэнда", "Вел'Коза", "Жанну", "Зайру", "Зерата", "Зилеана", "Карму", "Леону",
	"Лулу", "Люкс", "Мальфита", "Моргану", "Нами", "Наутилуса", "Пайка", "Рэйкана", "Свейна", "Сенну", "Сетта", "Сона", "Сораку",
	"Таам Кенча", "Тарика", "Треша", "Юми"]

motivations = ['. Я думаю, это будет легко', '. Я думаю, это будет просто', '. Я думаю, это не сложно', 
	'. Я думаю, ты справишься', '. Я верю в тебя', '. Ты справишься', '. Я думаю, ты сможешь', 
	'. Я уверен, ты сможешь', ". Я уверен, ты справишься", '. Посмотрим, что выйдет', '. Не думаю, что это будет сложно',
	'. Это будет весело', ", повеселишься", ', если кишка не тонка', ', если ты не очкуешь', ', если не ссыкло']

emojis = [':jigsaw:', ":skull_crossbones:", ":alien:", ":crown:", ":ok_hand_tone1:", ":call_me_tone1:", ':mechanical_arm:',
	":muscle_tone1:", ":fire:", ":earth_americas:", ":candy:", ":icecream:", ":butterfly:", ":moyai:", ":crossed_swords:", 
	":mega:", ":loudspeaker:", ":speech_balloon:", ":bell:"]

@Phil.event
async def on_ready():
	print ('Всё заебись!')

@Phil.event
async def on_member_join(member):
	add_start_role = discord.utils.get(member.guild.roles, id = 730771639788371968)
	await member.add_roles(add_start_role)

@Phil.command(aliases = ['admins'])
async def admin(ctx):
	await ctx.send(f'**#4708 Эльдар** :fleur_de_lis: \n**#5665 Филя** <:morgana:722944166262472734> \n**#0641 Тёма <:kayn:723183895100653638> ** \n**#1952 Даня** <:jinx:722932714977886298> \n**#6994 Аня** <:anya:722625155016163378>  ')


@Phil.command(pass_context=True)
async def change(ctx, lane: str = None):
	author = ctx.message.author
	if lane is None:
		champion = random.choice(champions)
		motivation = random.choice(motivations)
		emoji = random.choice(emojis)
		emoj = random.choice(emojis)
		await ctx.message.delete()
		await ctx.send(f"{emoj} {author.mention}, попробуй **{champion}**{motivation} {emoji}")
	elif lane == 'top':
		tp = random.choice(top)
		emoji = random.choice(emojis)
		emoj = random.choice(emojis)
		await ctx.message.delete()
		await ctx.send(f'{emoji} {author.mention}, возьми на топ **{tp}** {emoj}')
	elif lane == 'jungle':
		jg = random.choice(jungle)
		emoji = random.choice(emojis)
		emoj = random.choice(emojis)
		await ctx.message.delete()
		await ctx.send(f'{emoji} {author.mention}, возьми в лес **{jg}** {emoj}')
	elif lane == 'mid':
		md = random.choice(mid)
		emoji = random.choice(emojis)
		emoj = random.choice(emojis)
		await ctx.message.delete()
		await ctx.send(f'{emoji} {author.mention}, возьми на мид **{md}** {emoj}')
	elif lane == 'bot':
		bt = random.choice(bot)
		emoji = random.choice(emojis)
		emoj = random.choice(emojis)
		await ctx.message.delete()
		await ctx.send(f'{emoji} {author.mention}, возьми на бот **{bt}** {emoj}')
	elif lane == 'sup' or lane == 'support':
		sp = random.choice(support)
		emoji = random.choice(emojis)
		emoj = random.choice(emojis)
		await ctx.message.delete()
		await ctx.send(f'{emoji} {author.mention}, возьми поддержкой **{sp}** {emoj}')
	else:
		await ctx.message.delete()
		await ctx.send(f'**{author.mention}, неверно указана линия.** \n **```(top | jungle | mid | bot | support)```**')

@Phil.command(pass_context=True) 
async def help(ctx):
	author = ctx.message.author
	await ctx.send(f"Никто тебе не поможет, {author.mention}")

token = os.environ.get('BOT_TOKEN')
Phil.run(str(token))
