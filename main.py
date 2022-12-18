import nextcord
import datetime
import humanfriendly
from nextcord.ext import commands

settings = {
    'token': 'MTA1MjkyNzg4NTMyMjc0Nzk3NQ.GHaxch.pPNwd2XIiEiWgQU_su4AxpbRUECVo4BsBLts-s',
    'bot': 'SnOs',
    'id': 1052927885322747975,
    'prefix': '!'
}

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


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
async def unban(ctx, id, reason):
    user = await bot.fetch_user(id)
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
            "КиноАфиша"
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
        self.emUrl = nextcord.ui.TextInput(label="Ссылка на фильм", min_length=2, max_length=150, required=True,
                                           placeholder="Здесь вставьте ссылку на фильм")
        self.add_item(self.emUrl)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        title = self.emTitle.value
        desc = self.emDesc.value
        img = self.emImg.value
        url = self.emUrl.value
        em = nextcord.Embed(title=title, description=desc, url=url, color=0x5862f5)
        em.set_thumbnail(url=img)
        return await interaction.response.send_message(embed=em)


class Buttons(nextcord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    @nextcord.ui.button(label="Добавить фильм", style=nextcord.ButtonStyle.blurple)
    async def gray_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_modal(EmbedModal())


@bot.command()
async def button(ctx):
    embed2 = nextcord.Embed(title="Киноафиша",
                            description='Если вы хотите добавить фильм, то нажмите на кнопку --> "Добавить фильм"',
                            color=0x5862f5)
    await ctx.message.delete()
    await ctx.send(embed=embed2, view=Buttons())


# @bot.slash_command(name="name film", description="creat film", guild_ids=[927335861392146472])
# async def film(interaction: nextcord.Interaction):
#     await interaction.response.send_modal(EmbedModal())


bot.run(settings['token'])
