# Код написанные: RubiLom#3515

import nextcord
import datetime
import humanfriendly
from nextcord.ext import commands

settings = {
    'token': '',
    'bot': 'SnOs',
    'id': 1052927885322747975,
    'prefix': '!'
}

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(pass_contex=True)
async def ping(ctx):
    await ctx.send(f'Pong🎾 {ctx.author.mention}')


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


@bot.command()
@commands.has_any_role('Владелец', 'Разработчик')
async def dv(ctx, amount=2):
    await ctx.channel.purge(limit=amount + 1)


@bot.command(pass_contex=True)
@commands.has_any_role('Разработчик', 'Модератор', 'Владелец')
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
@commands.has_any_role('Разработчик', 'Владелец')
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
@commands.has_any_role('Разработчик', 'Владелец')
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
@commands.has_any_role('Разработчик', 'Владелец', 'Модератор')
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
@commands.has_any_role('Разработчик', 'Владелец', "Модератор")
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


@bot.command(pass_contex=True)
@commands.cooldown(1, 3600, commands.BucketType.user)
async def reqmeme(ctx, url):
    embed = nextcord.Embed(color=0x5862f5)
    embed.set_image(url=f"{url}")
    channel = bot.get_channel(1065295974911709234)
    await channel.send(f'{ctx.author.mention}')
    mojo = await channel.send(embed=embed)
    await mojo.add_reaction('👍🏻')
    await mojo.add_reaction('👎🏻')
    await ctx.message.delete()


@bot.command(pass_context=True)
async def gr(ctx, member: nextcord.Member):
    if ctx.author.name == 'Котик':
        guild_role = member.guild
        role = nextcord.utils.find(lambda r: r.name == 'Котик', guild_role.roles)
        if member.name == 'RubiLom':
            ctx.send('Вы не можете выдать данному игроку роль (Котик)')
        else:
            if role in member.roles:
                embed = nextcord.Embed(title='Убрана кастомная роль',
                                       description=f'Успешно убрана роль <@&1066014838867894354> участнику {member.mention}',
                                       color=0x5862f5)
                await member.remove_roles(role)
                await ctx.send(embed=embed)
            else:
                await member.add_roles(role)
                embed = nextcord.Embed(title='Выдана кастомная роль',
                                       description=f'Успешно выдана роль <@&1066014838867894354> участнику {member.mention}',
                                       color=0x5862f5)
                await ctx.send(embed=embed)


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
        await channel.send('''**!!!Заявка была принята!!!**
----------------------------------------------------------''')
        embed_accept = nextcord.Embed(title='Заявка на майнкрафт сервер **SN**',
                                      description=f'''Ваша заявка была **принята**!
Модератор: **{member.name}**
Теперь вам доступен этот канал <#1057601206840721458> со всей вам нужной информацией для захода на сервер!''',
                                      color=0x5862f5)
        channel_for_player = bot.get_channel(1055807362725843054)
        await channel_for_player.send(embed=embed_accept)


class Buttons4(nextcord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=timeout)

    @nextcord.ui.button(label="Отклонить", style=nextcord.ButtonStyle.red)
    async def red_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        member = interaction.user
        channel = bot.get_channel(1055462374234132490)
        await channel.send('''**!!!Заявка была отклонена!!!**
----------------------------------------------------------''')
        embed_declined = nextcord.Embed(title='Заявка на майнкрафт сервер **SN**',
                                        description=f'''Ваша заявка была **отклонена**!
Модератор: {member.name}
Так как ваша заявка была отклонена, вы можете ее переподать через неделю! (Пытаться раньше недели отправить заявку, приведет вас к муту/бану!)''',
                                        color=0x5862f5)
        channel_for_player = bot.get_channel(1055807362725843054)
        await channel_for_player.send(embed=embed_declined)


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
        self.emAd = nextcord.ui.TextInput(label="От куда вы узнали про нас?", min_length=1, max_length=1000,
                                          required=True,
                                          placeholder="Напишите от куда вы знаете нас!",
                                          style=nextcord.TextInputStyle.paragraph)
        self.add_item(self.emAd)
        self.emStudy = nextcord.ui.TextInput(label="Чем планируете заниматься?", min_length=1, max_length=1000,
                                             required=True,
                                             placeholder="Напишите чем планируете заниматься на сервере!",
                                             style=nextcord.TextInputStyle.paragraph)
        self.add_item(self.emStudy)
        self.emMod = nextcord.ui.TextInput(label="Какие моды/текстурпаки используете?", min_length=1, max_length=1000,
                                           required=True,
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
        channel_for_player = bot.get_channel(1055807362725843054)
        guild2 = member.guild
        role = nextcord.utils.get(guild2.roles, name="Ожидание")
        await member.add_roles(role)
        await channel.send(f'<@490518336547848213> | <@530108998381207562> --> {interaction.user.mention}')
        await channel.send(embed=em)
        await channel_for_player.send(embed=em_for_player)
        await channel_for_player.send(f'{interaction.user.mention}')
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


@bot.command()
async def button3(ctx):
    if ctx.author.name == 'RubiLom':
        embed3 = nextcord.Embed(title="Информация для новоприбывших игроков!",
                                description='''
ip: **playsn.tk**
Версия: **1.19.2**
Требуемые моды:
[SimpleVoice FORGE](https://www.curseforge.com/minecraft/mc-mods/simple-voice-chat/download/4271664) / [SimpleVoice FABRIC](https://www.curseforge.com/minecraft/mc-mods/simple-voice-chat/download/4271665)
[EmoteCraft FORGE](https://www.curseforge.com/minecraft/mc-mods/emotecraft-forge/download/4173796) / [EmoteCraft FABRIC](https://www.curseforge.com/minecraft/mc-mods/emotecraft/download/4173795)
[PlayerAnimator FORGE](https://www.curseforge.com/minecraft/mc-mods/playeranimator/download/4111521) / [PlayerAnimator FABRIC](https://www.curseforge.com/minecraft/mc-mods/playeranimator/download/4111522)
''',
                                color=0x5862f5)
        await ctx.message.delete()
        await ctx.send(embed=embed3)
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
    our_message_id = 1055554624964284516  # айди сообщения (сначала создаем его командой !react, а потом копируем его
    # айди и вписываем сюда)

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
```Также вы можете подписать каналы к вашему серверу зайдя на них и нажав на кнопку "Подписаться".```""",
                           color=0x5862f5)
    mojo = await channel.send(embed=embed)
    await mojo.add_reaction('🎁')
    await mojo.add_reaction('🎬')
    await mojo.add_reaction('📺')


# @bot.slash_command(name="name film", description="creat film", guild_ids=[927335861392146472])
# async def film(interaction: nextcord.Interaction):
#     await interaction.response.send_modal(EmbedModal())`

bot.run(settings['token'])
