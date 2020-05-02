import discord
import os
import requests
import json 
import time

def run_code(code,language):
        url = 'http://api.paiza.io:80/runners/'
        
        #running code
        create = 'create'
        post_data = {
            "source_code": code,
            "language":language,
            "api_key":"guest"
        }
        RunnigId = requests.post(url+create, data=post_data).json()['id']

        #check the status 
        r_stat = 'running'
        while not r_stat == 'completed':
            time.sleep(0.1)
            status = 'get_status'
            status_data = {'id':RunnigId,
                            'api_key':'guest'}
            r_stat = requests.get(url+status,params=status_data).json()['status']

        #get the successs or error result
        details = 'get_details'
        data = {'id':RunnigId,
                'api_key':'guest'}
        r_det = requests.get(url+details,params=data).json()
        return r_det
        

class code_runner(discord.Client):
    #ready to start up!
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    #when message comes!
    async def on_message(self,message):
        #pass when the message is own
        if message.author.bot:
            return
        
        #
        if message.content.startswith('!run'):
            content = message.content
            send = message.channel.send

            if content.count("```") != 2:
                return await send("SyntaxError: Missing ```")
            
            content = message.content.split("```")
            row1 = content[0].split()
            code = content[1]

            if len(row1) > 2: # too long syntax
                return await send('SyntaxError: please command as following\
                    ```\
                        !run <language> \
                    ```')
            elif len(row1) ==2:
                language = row1[1]
            else:
                language = 'python3'

            r_det = run_code(code,language)
            if r_det['stderr']:
                res = '```\n{}\n```'\
                    .format(r_det['stderr'])
                return await send(res)
                
            if r_det['stdout']:
                res = '```\n{}\nRunnnig time: {}\n```'\
                    .format(r_det['stdout'],r_det['time'])
                return await send(res)

if __name__ == "__main__":
    Token = os.environ.get("DISCORD_BOT_TOKEN")
    app = code_runner()
    app.run(Token)