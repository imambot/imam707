import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import asyncio

description = "Idk, something"
bot_prefix = "g."

client = commands.Bot(command_prefix=bot_prefix, description=description)

@client.event
async def on_ready():
    global playingsong, queue
    print("On Duty")
    print("Name :{}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print(discord.__version__)




@client.command(pass_context = True)
async def kick(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.kick_members:
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


@client.command(pass_context=True)
async def clear(ctx, number, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
         return

    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)

@client.command(pass_context = True)
async def getbans(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)





@client.command(pass_context=True)
async def stream(ctx):
    await client.say("https://www.twitch.tv/grossie_gore")

client.run("MzI5MjUwNzAyMDYyNzgwNDIw.DDP1tw.XNTAvXQK84ciQEiqeBlTw3uGwzs")
