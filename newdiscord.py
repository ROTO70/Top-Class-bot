import discord
import os
client = discord.Client()


@client.event
async def on_ready():
       print(client.user.id)
       print("ready")


@client.event
async def on_message(message):
     if message.content.startswith("안녕"):
         await message.channel.send("할말")


              
              
              
              
acces_token = os.environ["BOT_TOKEN"]              
client.run("access_token")
