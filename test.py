import discord


intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_presence_update(prev, cur: discord.Member):
    if cur.name == "uyuyuy" and cur.activity.name == 'Dota 2':
        channel = client.get_channel(942895908981473307)
        await channel.send('@everyone Dota<3')

client.run('NTA1Mzg1Mjc2MjczODUyNDM0.GsC6el.OBiqORd9SFrwkatuqdN_VNH3jnxN6HcwcqaJeM')
