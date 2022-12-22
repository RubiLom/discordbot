# Код написанные: RubiLom#3515
import random

import nextcord
import datetime
import humanfriendly
from nextcord.ext import commands
from tabulate import tabulate
import json
import sqlite3

settings = {
    'token': 'MTA1MjkyNzg4NTMyMjc0Nzk3NQ.GHaxch.pPNwd2XIiEiWgQU_su4AxpbRUECVo4BsBLts-s',
    'bot': 'SnOs',
    'id': 1052927885322747975,
    'prefix': '!'
}

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

#Экономика
# conn = sqlite3.connect("Discord.db") # или :memory:
# cursor = conn.cursor()
#
#
# @bot.event
# async def on_ready():
#     print("Bot Has been runned")#сообщение о готовности
#     for guild in bot.guilds:#т.к. бот для одного сервера, то и цикл выводит один сервер
#         print(guild.id)#вывод id сервера
#         serv=guild#без понятия зачем это
#         for member in guild.members:#цикл, обрабатывающий список участников
#             cursor.execute(f"SELECT id FROM users where id={member.id}")#проверка, существует ли участник в БД
#             if cursor.fetchone() is None:#Если не существует
#                 cursor.execute(f"INSERT INTO users VALUES ({member.id}, '{member.name}', '<@{member.id}>', 50000, 'S','[]',0,0)")#вводит все данные об участнике в БД
#             else:#если существует
#                 pass
#             conn.commit()#применение изменений в БД
#
#
# @bot.event
# async def on_member_join(member):
#     cursor.execute(f"SELECT id FROM users where id={member.id}")#все также, существует ли участник в БД
#     if cursor.fetchone() is None:#Если не существует
#         cursor.execute(f"INSERT INTO users VALUES ({member.id}, '{member.name}', '<@{member.id}>', 50000, 'S','[]',0,0)")#вводит все данные об участнике в БД
#     else:#Если существует
#         pass
#     conn.commit()#применение изменений в БД
#
#
# @bot.event
# async def on_message(message):
#     if len(message.content) > 10:#за каждое сообщение длиной > 10 символов...
#         for row in cursor.execute(f"SELECT xp,lvl,money FROM users where id={message.author.id}"):
#             exp=row[0]+random.randint(5, 40)#к опыту добавляется случайное число
#             cursor.execute(f'UPDATE users SET xp={exp} where id={message.author.id}')
#             lvch=exp/(row[1]*1000)
#             print(int(lvch))
#             lv=int(lvch)
#             if row[1] < lv:#если текущий уровень меньше уровня, который был рассчитан формулой выше,...
#                 await message.channel.send(f'Новый уровень!')#то появляется уведомление...
#                 bal=1000*lv
#                 cursor.execute(f'UPDATE users SET lvl={lv},money={bal} where id={message.author.id}')#и участник получает деньги
#     await bot.process_commands(message)#Далее это будет необходимо для ctx команд
#     conn.commit()#применение изменений в БД
#
#
# @bot.command()
# async def account(ctx):  # команда _account (где "_", ваш префикс указаный в начале)
#     table = [["nickname", "money", "lvl", "xp"]]
#     for row in cursor.execute(f"SELECT nickname,money,lvl,xp FROM users where id={ctx.author.id}"):
#         table.append([row[0], row[1], row[2], row[3]])
#         await ctx.send(f">\n{tabulate(table)}")
#
#
# @bot.command()
# async def inventory(ctx):  # команда _inventory (где "_", ваш префикс указаный в начале)
#
#     counter = 0
#     for row in cursor.execute(f"SELECT inventory FROM users where id={ctx.author.id}"):
#         data = json.loads(row[0])
#         table = [["id", "type", "name"]]
#         for row in data:
#             prt = row
#             for row in cursor.execute(f"SELECT id,type,name FROM shop where id={prt}"):
#                 counter += 1
#                 table.append([row[0], row[1], row[2]])
#
#                 if counter == len(data):
#                     await ctx.send(f'>\n{tabulate(table)}')
#
#
# @bot.command()
# async def shop(ctx):  # команда _shop (где "_", ваш префикс указаный в начале)
#     counter = 0
#     table = [["id", "type", "name", "cost"]]
#     for row in cursor.execute(f"SELECT id,type,name,cost FROM shop"):
#         counter += 1
#         table.append([row[0], row[1], row[2], row[3]])
#         if counter == 4:
#             await ctx.send(f'>\n{tabulate(table)}')
#
#
# async def buy(ctx, a: int):
#     uid = ctx.author.id
#     await ctx.send('Обработка... Если ответа не последует, указан неверный id предмета [buy {id}]')
#     for row in cursor.execute(f"SELECT money FROM users where id={uid}"):
#         money = row[0]
#         for row in cursor.execute(f"SELECT id,name,cost FROM shop where id={a}"):
#             cost = row[2]
#             if money >= cost:  # если у вас достаточно денег,то...
#                 money -= cost
#                 await ctx.send(f'Вы приобрели "{row[1]}" за {row[2]}')
#
#                 for row in cursor.execute(f"SELECT inventory FROM users where id={uid}"):
#                     data = json.loads(row[0])
#                     data.append(a)
#                     deed = json.dumps(data)
#                     cursor.execute('UPDATE users SET money=?,inventory = ? where id=?',
#                                    (money, deed, uid))  # добавляет предмет вам в инвентарь
#                     pass
#             if money < cost:  # иначе сообщает о недостатке
#                 await ctx.send(f'Недостаточно средств')
#                 pass
#     conn.commit()  # применение изменений в БД


@bot.command(pass_contex=True)
async def ping(ctx):
    await ctx.send(f'Pong🎾 {ctx.author.mention}')


# @bot.command(pass_contex=True)
# async def helping(ctx):
#     if ctx.author.name == 'RubiLom':
#         embed = nextcord.Embed(title="Команды Бота",
#                                description="""`!kick <@Участник> <Причина(без пробелов)>` - кикнуть участника.
# `!ban <@Участник> <Причина(без пробелов)>` - выдать бан участнику.
# `!unban <id(Через режим разработчика)> <Причина(без пробелов)>` - снять бан с участника.
# `!mute <@Участник> <время (в секундах)> <причина (без пробелов)>` - выдать мут участнику.
# `!unmute <@Участик> <Причина(без пробелов)>` - снять мут с участника""", color=0x5862f5)
#         await ctx.message.delete()
#         await ctx.send(embed=embed)
#     else:
#         pass


@bot.command(pass_contex=True)
async def helping2(ctx):
    if ctx.author.name == 'RubiLom':
        embed = nextcord.Embed(title="SnOS",
                               description='Все команды данного бота:', color=0x5862f5)
        embed.add_field(name="Кик участник", value="`!kick <@Участник> <Причина(без пробелов)>`",
                        inline=False)
        embed.add_field(name="Бан участника", value="`!ban <@Участник> <Причина(без пробелов)>`",
                        inline=False)
        embed.add_field(name="Разбан участника",
                        value="`!unban <id(Через режим разработчика)> <Причина(без пробелов)>`",
                        inline=False)
        embed.add_field(name="Мут участнику", value="`!mute <@Участник> <время (в секундах)> <причина (без пробелов)>`",
                        inline=False)
        embed.add_field(name="Размутить участника", value="`!unmute <@Участик> <Причина(без пробелов)>`",
                        inline=False)
        embed.set_footer(text=f"В случае ошибок пишите --> RubiLom#3515")
        await ctx.message.delete()
        await ctx.send(embed=embed)
    else:
        pass


@bot.command(pass_contex=True)
@commands.has_any_role('Разработчик', 'Администратор', 'Модератор', 'Основатель')
async def kick(ctx, member: nextcord.Member, reason=None):
    if member != ctx.author:
        embed2 = nextcord.Embed(description=f"""Вы были кикнуты с сервера!
Причина: **{reason}**
Модератор: {ctx.author.mention}""", color=0x5862f5)
        await ctx.message.delete()
        await member.send(embed=embed2)
        await member.kick(reason=reason)
        embed = nextcord.Embed(description=f"""Участник {member.mention} был кикнут c сервера
Причина: **{reason}**
Модератор: {ctx.author.mention}""", color=0x5862f5)

        await ctx.send(embed=embed)
    else:
        await ctx.send(f'Вы не можете кикнуть сами себя! {ctx.author.mention}')
        await ctx.message.delete()


@bot.command(pass_contex=True)
@commands.has_any_role('Разработчик', 'Администратор', 'Основатель')
async def ban(ctx, member: nextcord.Member, reason=None):
    if member != ctx.author:
        embed2 = nextcord.Embed(description=f"""Вы были забанены на сервере!
Причина: **{reason}**
Модератор: {ctx.author.mention}""", color=0x5862f5)
        await ctx.message.delete()
        await member.send(embed=embed2)
        await member.ban(reason=reason)
        embed = nextcord.Embed(description=f"""Участник {member.mention} был забанен
Причина: **{reason}**
Модератор: {ctx.author.mention}""", color=0x5862f5)

        await ctx.send(embed=embed)

    else:
        await ctx.message.delete()
        await ctx.send(f'Вы не можете забанить сами себя! {ctx.author.mention}')
        await ctx.message.delete()


@bot.command(pass_contex=True)
@commands.has_any_role('Разработчик', 'Администратор', 'Основатель')
async def unban(ctx, id_user, reason):
    user = await bot.fetch_user(id_user)
    embed = nextcord.Embed(description=f"""Участник {user} был разбанен
Причина: **{reason}**
Модератор: {ctx.author.mention}""", color=0x5862f5)

    try:
        await ctx.message.delete()
        await ctx.guild.unban(user)
        await ctx.send(embed=embed)

    except:
        ctx.send('Данный пользователь не забанен.')


@bot.command(pass_contex=True)
@commands.has_any_role('Разработчик', 'Администратор', 'Основатель', 'Модератор')
async def mute(ctx, member: nextcord.Member, time=None, reason=None):
    if member != ctx.author:
        time = humanfriendly.parse_timespan(time)
        await member.edit(timeout=nextcord.utils.utcnow() + datetime.timedelta(seconds=time))
        min_time = time / 60
        embed = nextcord.Embed(description=f"""Участник {member.mention} получил таймаут на **{min_time} min**
Причина: **{reason}**
Модератор: {ctx.author.mention}""", color=0x5862f5)
        embed2 = nextcord.Embed(description=f"""Вы получили таймаут на **{min_time} min**
Причина: **{reason}**
Модератор: {ctx.author.mention}""", color=0x5862f5)
        await ctx.message.delete()
        await member.send(embed=embed2)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f'Вы не можете кинуть в таймаут сами себя! {ctx.author.mention}')
        await ctx.message.delete()


@bot.command(pass_contex=True)
@commands.has_any_role('Разработчик', 'Администратор', 'Основатель', "Модератор")
async def unmute(ctx, member: nextcord.Member, reason=None):
    if member != ctx.author:
        embed = nextcord.Embed(description=f"""Участник {member.mention} был снят с таймаута
Причина: **{reason}**
Модератор: {ctx.author.mention}""", color=0x5862f5)
        embed2 = nextcord.Embed(description=f"""С вас сняли таймаут на сервере!
Причина: **{reason}**
Модератор: {ctx.author.mention}""", color=0x5862f5)
        await ctx.message.delete()
        await member.send(embed=embed2)
        await member.edit(timeout=None)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f'Вы не можете кинуть в таймаут сами себя! {ctx.author.mention}')
        await ctx.message.delete()


class EmbedModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Создайте свою КиноАфишу!"
        )

        self.emTitle = nextcord.ui.TextInput(label="Название фильма", min_length=2, max_length=50, required=True,
                                             placeholder="Здесь введите название фильма!")
        self.add_item(self.emTitle)
        self.emDesc = nextcord.ui.TextInput(label="Описание фильма", min_length=5, max_length=4000, required=True,
                                            placeholder="Здесь введите описание фильма!",
                                            style=nextcord.TextInputStyle.paragraph)
        self.add_item(self.emDesc)
        self.emImg = nextcord.ui.TextInput(label="Ссылка на фотографию", min_length=2, max_length=150, required=True,
                                           placeholder="Здесь вставьте ссылку на фотку(imgur)")
        self.add_item(self.emImg)
        self.emLink = nextcord.ui.TextInput(label="Совместный просмотр", min_length=2, max_length=150, required=True,
                                            placeholder="Вставьте ссылку на подключение к каналу!")
        self.add_item(self.emLink)
        self.emAward = nextcord.ui.TextInput(label="Награда", min_length=2, max_length=100, required=True,
                                             placeholder="Введите какая будет награда за просмотр фильма/сериала")
        self.add_item(self.emAward)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        title = self.emTitle.value
        desc = self.emDesc.value
        img = self.emImg.value
        link = self.emLink.value
        award = self.emAward.value
        em = nextcord.Embed(title=title, description=f"{desc} | [Совместный просмотр!]({link})", color=0x5862f5)
        em.set_thumbnail(url=img)
        em.set_footer(text=f"Награда за просмотр: {award} монет!")
        channel = bot.get_channel(1053990199039897630)
        await channel.send('<@&1053654174870544394>')
        await channel.send(embed=em)


class Buttons(nextcord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=timeout)

    @nextcord.ui.button(label="Добавить фильм", style=nextcord.ButtonStyle.blurple)
    async def blue_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_modal(EmbedModal())

class Buttons2(nextcord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=timeout)

    @nextcord.ui.button(label="Подать заявку!", style=nextcord.ButtonStyle.blurple)
    async def blue_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_modal(EmbedModal2())


class Buttons3(nextcord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=timeout)

    @nextcord.ui.button(label="Принять", style=nextcord.ButtonStyle.green)
    async def green_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        member = interaction.user
        channel = bot.get_channel(1055462374234132490)
        embed_accept = nextcord.Embed(title='Заявка на майнкрафт сервер **SN**',
                                      description=f'''Ваша заявка была **принята**!
Модератор: **{member.name}**
Айпи сервера: **playsn.tk**
Нужные моды: [SimpleVoice](https://www.curseforge.com/minecraft/mc-mods/simple-voice-chat), [EmoteCraft FORGE](https://www.curseforge.com/minecraft/mc-mods/emotecraft-forge) / [EmoteCraft FABRIC](https://www.curseforge.com/minecraft/mc-mods/emotecraft)''', color=0x5862f5)
        await member.send(embed=embed_accept)
        await channel.send('''**!!!Заявка была принята!!!**
----------------------------------------------------------''')


class Buttons4(nextcord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=timeout)

    @nextcord.ui.button(label="Отклонить", style=nextcord.ButtonStyle.red)
    async def red_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        member = interaction.user
        channel = bot.get_channel(1055462374234132490)
        embed_declined = nextcord.Embed(title='Заявка на майнкрафт сервер **SN**',
                                      description=f'''Ваша заявка была **отклонена**!
Модератор: {member.name}
Так как ваша заявка была отклонена, вы можете ее переподать через неделю! (Пытаться раньше недели отправить заявку, приведет вас к муту/бану!)''', color=0x5862f5)
        await member.send(embed=embed_declined)
        await channel.send('''**!!!Заявка была отклонена!!!**
----------------------------------------------------------''')


class EmbedModal2(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Заявка на сервер SN!"
        )

        self.emNick = nextcord.ui.TextInput(label="Игровой никнейм", min_length=2, max_length=50, required=True,
                                             placeholder="Введите ваш игровой никнейм!")
        self.add_item(self.emNick)
        self.emOld = nextcord.ui.TextInput(label="Сколько вам лет?", min_length=1, max_length=10, required=True,
                                             placeholder="Напишите сколько вам лет? (Пример: 16)")
        self.add_item(self.emOld)
        # self.emHobby = nextcord.ui.TextInput(label="Хобби", min_length=1, max_length=1000, required=True,
        #                                      placeholder="Напишите какие ваши любимые хобби!",
        #                                      style=nextcord.TextInputStyle.paragraph)
        # self.add_item(self.emHobby)
        self.emAd = nextcord.ui.TextInput(label="От куда вы узнали про нас?", min_length=1, max_length=1000, required=True,
                                             placeholder="Напишите от куда вы знаете нас!",
                                             style=nextcord.TextInputStyle.paragraph)
        self.add_item(self.emAd)
        self.emStudy = nextcord.ui.TextInput(label="Чем планируете заниматься?", min_length=1, max_length=1000, required=True,
                                             placeholder="Напишите чем планируете заниматься на сервере!",
                                             style=nextcord.TextInputStyle.paragraph)
        self.add_item(self.emStudy)
        self.emMod = nextcord.ui.TextInput(label="Какие моды/текстурпаки используете?", min_length=1, max_length=1000, required=True,
                                             placeholder="Напишите какие моды/текстурпаки используете!",
                                             style=nextcord.TextInputStyle.paragraph)
        self.add_item(self.emMod)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        member = interaction.user
        nick = self.emNick.value
        old = self.emOld.value
        ad = self.emAd.value
        study = self.emStudy.value
        em = nextcord.Embed(title='Новая заявка на сервер!', description=f'''
        Никнейм: {nick}
        Возраст: {old} лет
        От куда узнал: {ad}
        Чем планирует заниматься: {study}
        ''', color=0x5862f5)
        em_for_player = nextcord.Embed(title='Заявка на майнкрафт сервер **SN**',
                                       description='Ваша заявка отправлена, ожидайте, в скором времени её проверят!',
                                       color=0x5862f5)
        channel = bot.get_channel(1055462374234132490)
        try:
            await member.send(embed=em_for_player)
        except:
            pass

        await channel.send(f'<@490518336547848213> | <@530108998381207562> --> {interaction.user.mention}')
        await channel.send(embed=em)
        await channel.send(view=Buttons3())
        await channel.send(view=Buttons4())


@bot.command()
async def button(ctx):
    if ctx.author.name == 'RubiLom':
        embed2 = nextcord.Embed(title="Киноафиша",
                                description='Если вы хотите добавить фильм, то нажмите на кнопку --> "Добавить фильм"',
                                color=0x5862f5)
        await ctx.message.delete()
        await ctx.send(embed=embed2, view=Buttons())
    else:
        pass


@bot.command()
async def button2(ctx):
    if ctx.author.name == 'RubiLom':
        embed2 = nextcord.Embed(title="Заявка на сервер!",
                                description='Если вы хотите попасть на наш майнкрафт сервер то нажмите на кнопку!',
                                color=0x5862f5)
        await ctx.message.delete()
        await ctx.send(embed=embed2, view=Buttons2())
    else:
        pass


@bot.event
async def on_raw_reaction_add(payload):
    our_message_id = 1055554624964284516  # айди сообщения (сначала создаем его командой !react, а потом копируем его
    # айди и вписываем сюда)

    if our_message_id == payload.message_id:
        member = payload.member  # определяем юзера
        guild1 = member.guild  # определяем сервер

        emoji = payload.emoji.name  # эмоджи при нажатии на которое выдается роль
        if emoji == '🎁':  # само эмоджи
            role = nextcord.utils.get(guild1.roles, name="🎁")  # определяем роль которую будем выдавать
            await member.add_roles(role)  # выдаем рольку

        elif emoji == '🎬':  # само эмоджи
            role = nextcord.utils.get(guild1.roles, name="🎬")  # определяем роль которую будем выдавать
            await member.add_roles(role)  # выдаем рольку

        elif emoji == '📺':  # само эмоджи
            role = nextcord.utils.get(guild1.roles, name="📺")  # определяем роль которую будем выдавать
            await member.add_roles(role)  # выдаем рольку


@bot.event
async def on_raw_reaction_remove(payload):
    our_message_id = 1055554624964284516  # айди сообщения (сначала создаем его командой !react, а потом копируем его айди и вписываем сюда)

    if our_message_id == payload.message_id:
        guild1 = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name  # эмоджи при нажатии на которое выдается роль
        if emoji == '🎁':  # само эмоджи
            role = nextcord.utils.get(guild1.roles, name="🎁")

            member = await(guild1.fetch_member(payload.user_id))
            if member is not None:
                await member.remove_roles(role)
            else:
                print('not found')

        elif emoji == '🎬':  # само эмоджи
            role = nextcord.utils.get(guild1.roles, name="🎬")

            member = await(guild1.fetch_member(payload.user_id))
            if member is not None:
                await member.remove_roles(role)
            else:
                print('not found')

        elif emoji == '📺':  # само эмоджи
            role = nextcord.utils.get(guild1.roles, name="📺")

            member = await(guild1.fetch_member(payload.user_id))
            if member is not None:
                await member.remove_roles(role)
            else:
                print('not found')


@bot.command()
async def react(ctx):
    channel = bot.get_channel(1037105214974591056)
    embed = nextcord.Embed(description="""```           ⠀         Роли уведомлений                    ```
> <@&1055549927838720011> — <#1055550642665553971>
> <@&1053654174870544394> — <#1053990199039897630>
> <@&930252257067425912> — <#1037106184907395173>
```Также вы можете подписать каналы к вашему серверу зайдя на них и нажав на кнопку "Подписаться".```""", color=0x5862f5)
    mojo = await channel.send(embed=embed)
    await mojo.add_reaction('🎁')
    await mojo.add_reaction('🎬')
    await mojo.add_reaction('📺')




# @bot.slash_command(name="name film", description="creat film", guild_ids=[927335861392146472])
# async def film(interaction: nextcord.Interaction):
#     await interaction.response.send_modal(EmbedModal())`

bot.run(settings['token'])
