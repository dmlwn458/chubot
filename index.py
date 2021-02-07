import discord
import random
import os


client = discord.Client()

@client.event
async def on_ready():
    print('client is Ready')
    await client.change_presence(status = discord.Status.online, activity = discord.game('당신을 생각하는 중'))
    

@client.event
async def on_message(message):
     if message.content == 'test': 
        a = ['안녕', '안녕하십니까!', '하이', '안녕하세요']
        await message.channel.send(random.choice(a))

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
