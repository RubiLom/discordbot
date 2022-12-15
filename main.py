import nextcord
import time
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
        embed2 = nextcord.Embed(title=f"Кик с сервера **SN**",
                                description=f"""Вы были кикнуты этим администратором: {ctx.author.mention}
Причина: **{reason}**""", color=0x5862f5)
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
        embed2 = nextcord.Embed(title=f"Бан на сервера **SN**",
                                description=f"""Вы были забанены этим администратором: {ctx.author.mention}
Причина: **{reason}**""", color=0x5862f5)
        await member.send(embed=embed2)
        await member.ban(reason=reason)
        embed = nextcord.Embed(title=f"Был забанен {member.name}",
                               description=f"""{member.mention} был забанен этим администратором: {ctx.author.mention}
Причина: **{reason}**""", color=0x5862f5)

        await ctx.send(embed=embed)

    else:
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
        await ctx.guild.unban(user)
        await ctx.send(embed=embed)
    except:
        ctx.send('Данный пользователь не забанен.')


# @bot.command(pass_contex=True)
# @commands.has_any_role('Разработчик', 'Администратор', 'Основатель')
# async def timeout(ctx, member=nextcord.Member, timeout=None, reason=None):
#     if member != ctx.author:
#         embed = nextcord.Embed(title=f"Был кинут в таймаут {member}",
#                                description=f"""{member.mention} был кинут в таймаут этим администратором: {ctx.author.mention}
# Причина: **{reason}**
# Сроком: **{timeout}**""", color=0x5862f5)
#         embed2 = nextcord.Embed(title=f"Таймаут на сервере **SN**",
#                                 description=f"""Вы были кинуты в таймаут этим администратором: {ctx.author.mention}
# Причина: **{reason}**
# Сроком: **{timeout}**""", color=0x5862f5)
#         await member.send(embed=embed2)
#         await timeout(timeout=timeout, reason=reason)
#         await ctx.send(embed=embed)
#     else:
#         await ctx.send(f'Вы не можете кинуть в таймаут сами себя! {ctx.author.mention}')
#         await ctx.message.delete()


bot.run(settings['token'])
