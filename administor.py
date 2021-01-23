import discord
import random
from discord.ext import commands
from discord import User
from discord.ext.commands import Bot, guild_only

TOKEN = "Nzk5MzA4OTIwMTE5ODg1ODU0.YABscA.rXXrWBFWckHyeQYF8gbmIHAAD04"

client = commands.Bot(command_prefix='.')


# bot çalıştığında / #bot status
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("YAPIM AŞAMASINDA!"))
    print("Bot is online..")


# Delete Message
@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(title=".clear", description="Mesajlar silindi!")
    await ctx.send(embed=embed)


# Kicked
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
    await user.kick(reason=reason)
    await ctx.send(f"{user} kicklenmiştir.")


# Banned
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
    await user.ban(reason=reason)
    await ctx.send(f"{user} banlanmıştır.")


# unbanned
@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Ban kaldırıldı {user.mention}')
            return


# mute
@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member):
    muteRole = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(muteRole)
    embed = discord.Embed(title=f"{member.mention}, muted!")
    await ctx.send(embed=embed)


# mute handling
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed()
        embed.add_field(name="Mutelemek istediğiniz kişiyi etiketleyiniz.", value=".mute @EXAMPLE", inline=True)
        await ctx.send(embed=embed)


# unmute
@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    muteRole = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(muteRole)
    await ctx.send(f"{member.mention}, mutesi açıldı.")


# unmute handling
@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed()
        embed.add_field(name="Mutesini açmak istediğiniz kişiyi etiketleyiniz.", value=".unmute @EXAMPLE", inline=True)
        await ctx.send(embed=embed)


# Change nick
@client.command(pass_context=True)
async def chnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')


# ROL VERMEK
@client.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"{ctx.author.name} , {user.name} isimli üyeye bir rol verdi: {role.name}")


# rol oluşturmak
@client.command(aliases=['make_role'])
@commands.has_permissions(manage_roles=True)
async def create_role(ctx, *, name):
    guild = ctx.guild
    await guild.create_role(name=name)
    await ctx.send(f'`{name}` Rolü oluşturuldu')


# burayı geliştir
@client.command("invite")
async def invite(prfx):
    embed = discord.Embed(title="TIKLA VEYA KOPYALA", url="https://discord.gg/qUmrynGp9X",
                          description="https://discord.gg/qUmrynGp9X")
    await prfx.send(embed=embed)


# Help
@client.command()
async def yardim(prfx):
    embed = discord.Embed(title="𝐁𝐎𝐓 𝐊𝐎𝐌𝐔𝐓", url="https://discord.gg/bw4ZwYEB", color=0x050505)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/785816245919678533/797795155251167262/b6c2b121ba34e404f68dcc8384753acb.jpg")
    embed.add_field(name="🚫 Moderasyon Komutları:", value=".admin", inline=False)
    embed.add_field(name="😂 Eğlence Komutları:", value=".eğlence", inline=False)
    embed.add_field(name="📩 Sunucu davet Linki:", value=".davet", inline=False)
    embed.add_field(name="📷 Resim Komutları:", value=".resim", inline=False)
    embed.add_field(name="🔞 NSWF Komutları:", value=".nswf", inline=False)
    embed.add_field(name="📧 İletişim Komutları:", value=".iletisim", inline=False)
    await prfx.send(embed=embed)


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed()
        embed.add_field(name="Mutelemek istediğiniz kişiyi etiketleyiniz.", value=".mute @EXAMPLE", inline=True)
        await ctx.send(embed=embed)


client.run(TOKEN)
