import discord
import os
import request
import flask

Token = os.environ("DISCORD_BOT_TOKEN")

class code_runner(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_Message(self,message):
        if message.author==self.user:
            return
        
        if message.content.startswith('!run'):
            await message.channel.send('Hello')

# def run_code():
#     url = 'http://api.paiza.io:80/runners/'
#     cre = 'create'
#     detail = 'get_detail'
#     response = request.post()
app = code_runner()
app.run(Token)