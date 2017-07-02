import discord
from discord.ext import commands
import time

description = "Idk, something"
bot_prefix = "i."
listsomethin = ["england"]
kappalist = ["kappa"]

client = commands.Bot(command_prefix=bot_prefix, description=description)

@client.event
async def on_ready():
    global playingsong, queue
    print("On Duty")
    print("Name :{}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print(discord.__version__)


@client.event
async def on_message(message):
    if message.content in kappalist:
        emoji = discord.utils.get(message.server.emojis, id='301806377414819841')
        await client.add_reaction(message, emoji)


@client.command(pass_context = True)
async def kick(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return

    if not member:
        return await client.say(ctx.message.author.mention + " Specify a user to kick!")
    try:
        await client.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")

    embed = discord.Embed(description = "**%s** has been kicked!"%member.name, color = 0xFF0000)
    return await client.say(embed = embed)



@client.command(pass_context = True)
async def ban(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return

    if not member:
        return await client.say(ctx.message.author.mention + " Specify a user to ban!")
    try:
        await client.ban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")

    embed = discord.Embed(description = "**%s** has been banned!"%member.name, color = 0xFF0000)
    return await client.say(embed = embed)


@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author.id == "328968305098489856":
        pass
    else:
        somethin = message.content.lower()
        listsomethin = somethin.split()
        if "england" in listsomethin:
            await client.send_message(client.get_channel(message.channel.id), 'ENGLAND IS MY CITY')


@client.command(pass_context=True)
async def wiz(ctx):
    await client.say("http://i.imgur.com/DINoQ8P.jpg")




client.run("MzI4OTY4MzA1MDk4NDg5ODU2.DDLnIQ.m8INUu0_b8fnrfDZDr1nr9B4-ig")
