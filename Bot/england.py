import discord
from discord.ext import commands
import time
import asyncio
import random
import io

client = commands.Bot('i.')
goodnight_list = ["gn", "good night", "goodnight"]
goodmorning_list = ["gm", "goodmorning", "good morning"]

minutes = 0
hour = 0

@client.event
async def on_ready():
    global playingsong, queue
    print("On Duty")
    print("Name :{}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print(discord.__version__)

async def tutorial_uptime():
    await client.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not client.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1




@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "kappa" in message.content.lower():
        emoji = discord.utils.get(message.server.emojis, id='301806377414819841')
        await client.add_reaction(message, emoji)

    if "thonk" in message.content.lower():
        emoji = discord.utils.get(message.server.emojis, id='325660866106097664')
        await client.add_reaction(message, emoji)

    if "england" in message.content.lower():
            await client.send_message(message.channel, 'ENGLAND IS MY CITY')


    if message.content.lower() in goodnight_list:
        IDK =  await client.send_message(message.channel, 'Good Night !')
        await asyncio.sleep(2)
        await client.delete_message(IDK)

    if message.content.lower() in goodmorning_list:
        IDK =  await client.send_message(message.channel, 'Good Morning !')
        await asyncio.sleep(2)
        await client.delete_message(IDK)

    if message.content.startswith('i.uptime'):
        await client.send_message(message.channel, "`I've been online for {0} hour(s) and {1} minutes in {2}. `".format(hour, minutes, message.server))

    if message.content.startswith('i.user'):
        try:
            user = message.mentions[0]
            userjoinedat = str(user.joined_at).split('.', 1)[0]
            usercreatedat = str(user.created_at).split('.', 1)[0]

            userembed = discord.Embed(
                title="Username:",
                description=user.name,
                color=0xe67e22
            )
            userembed.set_author(
                name="User Info"
            )
            userembed.add_field(
                name="Joined the server at:",
                value=userjoinedat
            )
            userembed.add_field(
                name="User Created at:",
                value=usercreatedat
            )
            userembed.add_field(
                name="Discriminator:",
                value=user.discriminator
            )
            userembed.add_field(
                name="User ID:",
                value=user.id
            )

            await client.send_message(message.channel, embed=userembed)
        except IndexError:
            await client.send_message(message.channel, "I couldn't find anyone.")
        except:
            await client.send_message(message.channel, "Sorry Error")
        finally:
            pass



@client.event
async def on_member_join(member):
    serverchannel = member.server.default_channel
    msg = "**Welcome {0} to {1}**".format(member.mention, member.server.name)
    await client.send_message(serverchannel, msg)

@client.event
async def on_member_remove(member):
    serverchannel = member.server.default_channel
    msg = "**{0} just left, bye bye !**".format(member.mention)
    await client.send_message(serverchannel, msg)


client.loop.create_task(tutorial_uptime())
client.run("MzI4OTY4MzA1MDk4NDg5ODU2.DDbpzA.vHVu1w3oEjBj0HJysKqaexOnfFw")
