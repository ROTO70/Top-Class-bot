import discord

client = discord.Client()


@client.event
async def on_ready():
       print(client.user.id)
       print("ready")


@client.event
async def on_message(message):
     if message.content.startswith("안녕"):
         await message.channel.send("할말")


client.run("NjU3OTA4MjY0MDc5NDU4MzE1.Xf4DKQ.w9LmrZtVnaVid7Gr1-TVX6r1_Ek")



