import discord
import os
import request

Token = os.environ("DISCORD_BOT_TOKEN")

client = discord.Client()
@client.event()
async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

@client.event()
async def on_Message(message):
    if message.author.bot:
        return
    
    if message.content.startswith('!run'):
        await message.channel.send('Hello')

client.run(Token)