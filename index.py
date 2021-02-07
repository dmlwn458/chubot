import discord
import random
client = discord.Client()
token = 'ODA3ODU0ODc2MjkzODU3Mjkw.YB-Dew.D_Or-RuKU3mFdI4g-e9nnC6VolM'

@client.event
async def on_ready():
    print('client is Ready')
    await client.change_presence(status = discord.Status.online, activity = discord.game('당신을 생각하는 중'))
    

@client.event
async def on_message(message):
     if message.content == 'test': 
        a = ['안녕', '안녕하십니까!', '하이', '안녕하세요']
        await message.channel.send(random.choice(a))


client.run(token)