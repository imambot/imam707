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

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "lads" in message.content.lower():
            await client.send_message(message.channel, 'BOYS')


client.run("MzI5MjUwNzAyMDYyNzgwNDIw.DDP1tw.XNTAvXQK84ciQEiqeBlTw3uGwzs")
