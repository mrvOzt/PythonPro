import discord
from password import gen_pass



# İstekler değişkeni botun yetkilerini saklar
intents = discord.Intents.default()
# Mesaj okuma yetkisini etkinleştirme
intents.message_content = True
# Bir bot oluşturma ve yetkileri aktarma
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yapıldı')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Merhaba!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$sifre'):
         await message.channel.send(gen_pass(25))
    

client.run("MTE1ODA2MTUwNTIwODY2MDA3OA.GiRQ-Y.rSGkvR05mF9vZ7dh3tH9KEbQlzLlkpUM8asD-8")
