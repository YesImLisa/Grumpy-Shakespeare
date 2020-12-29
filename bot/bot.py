import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '/')

# First Event
@client.event
async def on_ready():
    print('Shakespeare is ready!')

client.run('NzkzMjkwNDI4Njc3NzUwNzg0.X-qHSA.cnIf-1fCDbFAwnC1FIKggyUoqEU') # Token
