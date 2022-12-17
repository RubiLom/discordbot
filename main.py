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


@bot.command(pass_contex=True)
@commands.has_any_role('Разработчик', 'Администратор', 'Модератор', 'Основатель')
async def kick(ctx, member: nextcord.Member, reason=None):
    if member != ctx.author:
        embed2 = nextcord.Embed(title=f"Кик с сервера",
                                description=f"""Вы были кикнуты этим администратором: {ctx.author.mention}
Причина: **{reason}**""", color=0x5862f5)
        await ctx.message.delete()
        await member.send(embed=embed2)
        await member.kick(reason=reason)
        embed = nextcord.Embed(title=f"Был кикнут {member.name}",
                               description=f"""{member.mention} был кикнут этим администратором: {ctx.author.mention}
Причина: **{reason}**""", color=0x5862f5)

        await ctx.send(embed=embed)
    else:
        await ctx.send(f'Вы не можете кикнуть сами себя! {ctx.author.mention}')
        await ctx.message.delete()


@bot.command(pass_contex=True)
@commands.has_any_role('Разработчик', 'Администратор', 'Основатель')
async def ban(ctx, member: nextcord.Member, reason=None):
    if member != ctx.author:
        embed2 = nextcord.Embed(title=f"Бан на сервера",
                                description=f"""Вы были забанены этим администратором: {ctx.author.mention}
Причина: **{reason}**""", color=0x5862f5)
        await ctx.message.delete()
        await member.send(embed=embed2)
        await member.ban(reason=reason)
        embed = nextcord.Embed(title=f"Был забанен {member.name}",
                               description=f"""{member.mention} был забанен этим администратором: {ctx.author.mention}
Причина: **{reason}**""", color=0x5862f5)

        await ctx.send(embed=embed)

    else:
        await ctx.message.delete()
        await ctx.send(f'Вы не можете забанить сами себя! {ctx.author.mention}')
        await ctx.message.delete()


@bot.command(pass_contex=True)
@commands.has_any_role('Разработчик', 'Администратор', 'Основатель')
async def unban(ctx, id):
    user = await bot.fetch_user(id)
    embed = nextcord.Embed(title=f"Был разбанен {user}",
                           description=f"""{user} был разбанен этим администратором: {ctx.author.mention}""",
                           color=0x5862f5)
    try:
        await ctx.message.delete()
        await ctx.guild.unban(user)
        await ctx.send(embed=embed)

    except:
        ctx.send('Данный пользователь не забанен.')


@bot.command(pass_contex=True)
@commands.has_any_role('Разработчик', 'Администратор', 'Основатель')
async def mute(ctx, member: nextcord.Member, time=None, reason=None):
    if member != ctx.author:
        time = humanfriendly.parse_timespan(time)
        await member.edit(timeout=nextcord.utils.utcnow() + datetime.timedelta(seconds=time))
        min_time = time / 60
        embed = nextcord.Embed(title=f"Был кинут в таймаут {member.name}",
                               description=f"""{member.mention} был кинут в таймаут этим администратором: {ctx.author.mention}
Причина: **{reason}**
Сроком: **{min_time} min**""", color=0x5862f5)
        embed2 = nextcord.Embed(title=f"Таймаут на сервере",
                                description=f"""Вы были кинуты в таймаут этим администратором: {ctx.author.mention}
Причина: **{reason}**
Сроком: **{min_time} min**""", color=0x5862f5)
        await ctx.message.delete()
        await member.send(embed=embed2)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f'Вы не можете кинуть в таймаут сами себя! {ctx.author.mention}')
        await ctx.message.delete()


@bot.command(pass_contex=True)
@commands.has_any_role('Разработчик', 'Администратор', 'Основатель')
async def unmute(ctx, member: nextcord.Member, reason=None):
    if member != ctx.author:
        embed = nextcord.Embed(title=f"Был снят с таймаута {member.name}",
                               description=f"""{member.mention} был снят с таймаута этим администратором: {ctx.author.mention}
Причина: {reason}""", color=0x5862f5)
        embed2 = nextcord.Embed(title=f"Снят таймаут на сервере",
                                description=f"""С вас сняли таймаут этим администратором: {ctx.author.mention}
Причина: {reason}""", color=0x5862f5)
        await ctx.message.delete()
        await member.send(embed=embed2)
        await member.edit(timeout=None)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f'Вы не можете кинуть в таймаут сами себя! {ctx.author.mention}')
        await ctx.message.delete()


bot.run(settings['token'])
