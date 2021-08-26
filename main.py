coin = ["орёл", "решка"]
ansers = ["Привет", "Здравствуй", "О,какие люди!", "Привет, рад тебя видеть", "Наконец-то ты вернулся!"]
import discord
from discord.utils import get
import random
TOKEN = 'ODY4MDYwMzkyNjkyMjYwODg1.YPqKPQ.fMRCRLzgbkuqgRgH7B0IdvCkOUg'
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
@client.event
async def prepare_game(ctx):
    guild = ctx.guild
    role = await guild.create_role(name=role_name)
    category = await guild.create_category('Game')
    await category.set_permissions(role, read_messages=True, send_messages=True, connect=True, speak=True)
    await category.set_permissions(ctx.guild.me, read_messages=True, send_messages=True, speak=True)
    text_channel = await guild.create_text_channel('Board', category=category, sync_permissions=True)
    voice_channel = await guild.create_voice_channel('Room', category=category, sync_permissions=True)
@client.event
async def on_voice_state_update(member, before, after):
    if not before.channel and after.channel:
        role = discord.utils.get(member.guild.roles, name="human")
        print(role)
        await member.add_roles(role)
    elif before.channel and not after.channel:
        role = discord.utils.get(member.guild.roles, name="human")
        await member.remove_roles(role)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
@client.event
async def on_message(message):
    channel = message.channel
    user_message = message.content.lower()
    if user_message.find("прив")== True:
        await channel.send(random.choice(ansers))
client.run(TOKEN)
