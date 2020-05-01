import discord
import os
import request

class code_runner(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_Message(self,message):
        if message.author.bot:
            return
        
        print('Hello')
        if message.content.startswith('!run'):
            await message.channel.send('Hello')

# def run_code():
#     url = 'http://api.paiza.io:80/runners/'
#     cre = 'create'
#     detail = 'get_detail'
#     response = request.post()
if __name__ == "__main__":
    Token = os.environ["DISCORD_BOT_TOKEN"]
    app = code_runner()
    app.run(Token)