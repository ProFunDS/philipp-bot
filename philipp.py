  
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import random

Phil = commands.Bot(command_prefix= "dl.")
Phil.remove_command('help')

champions = ['Азира', 'Акали', 'Алистара', 'Амуму', 'Анивию', 'Ари', 'Атрокса', 'Аурелион Сола', "Афелия",
	"Барда", "Блицранка", "Браума", "Брэнда", "Вай", "Варвика :wolf: ", "Варуса", "Вейгара", "Вейн", "ВелКоза", 
	"Владимира", "Волибира", "Вуконга", "Галио", "Гангпланка", "Гарена", "Гекарима :horse_racing_tone1:", "Гнара", 
	"Грагаса", "Грейвза", "Дариуса", "Джакса", "Джарвана", "Джейса", "Джина", "Джинкс", "Диану", "Доктора Мундо", 
	"Дрейвена", "Жанну", "Зайру", "Зака", "Зеда", "Зерата", "Зиггса", "Зилеана", "Зои", "Иверна", "Иллаой", "Ирелию", 
	"Йорика", "КаЗикса", "Каина", "КайСу", "Калисту", "Камиллу", "Карму", "Картуса", "Кассадина", "Кассиопею", "Катарину", 
	"Квинн", "Кейл", "Кейтлин", "Кеннена", "Киану", "Киндред", "Кледа", "КогМао", "Корки", "Ксин Жао", "Ле Блан", "Леону", 
	"Ли Сина", "Лиссандру", "Лулу", "Люкс", "Люциана", "Мальзахара", "Мальфита", "Маойкая", "Мастера Йи", "Мисс Фортуну", 
	"Моргану", "Мордекайзера", "Нами", "Насуса", "Наутилуса", "Нидали :tiger:", "Нико :lizard:", "Ноктюрна", "Нуну и Виллумпа", 
	"Орианну :robot: ", "Орна", "Пайка", "Пантеона", "Поппи", "Райза", "Рамбла", "Раммуса", "РекСай", "Ренгара", "Ренектона", 
	"Ривен", "Рэйкана", "Сайласа", "Свейна", "Седжуани", "Сенну", "Сетта", "Сивир", "Синджеда", "Синдру", "Сиона", "Скарнера", 
	"Сону", "Сораку", "Таам Кенча", "Талию", "Талона", "Тарика", "Твистед Фэйта", "Твича", "Тимо :japanese_ogre:", "Трандла", 
	"Треша", "Триндамира", "Тристану", "Удира", "Ургота", "Фиддлстикса", "Физза", "Фиору :person_fencing:", "Хеймердингера", 
	"ЧоГата", "Шако", "Шаю", "Шена", "Шивану", "Эвелинн", "Эзреаля", "Экко", "Элизу", "Энни :fire:", "Эш", "Юми :smirk_cat:", 
	"Ясуо :man_in_manual_wheelchair_tone1:", "Лиллию", 'Олафа', "Виктора"]

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
	await ctx.send(f'**#4708 Эльдар** :fleur_de_lis: \n**#5665 Филя** <:morgana:722944166262472734> \n**#0641 Тёма <:kayn:723183895100653638>** \n**#1952 Даня** <:jinx:722932714977886298> \n**#6994 Аня** <:anya:722625155016163378>')

@Phil.command(pass_context=True)
async def change(ctx):
	champion = random.choice(champions)
	motivation = random.choice(motivations)
	emoji = random.choice(emojis)
	emoj = random.choice(emojis)
	await ctx.send(f"{emoj} Попробуй **{champion}**{motivation} {emoji}")

@Phil.command(pass_context=True) 
async def help(ctx):
	author = ctx.message.author
	await ctx.send(f"Никто тебе не поможет, {author.mention}")

token = os.environ.get('BOT_TOKEN')
Phil.run(str(token))
