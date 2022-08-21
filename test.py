from random import seed
from random import randint
import discord


intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
seed(1)

nicks = ['uyuyuy', 'Yarre']
games = ['dota 2', 'Wallpaper Engine']
data = ['uyuyuy', False]
messages = ['@everyone , {0} goes {1}. Go with him!',
            '@everyone  I({0}) want to play {1}. Go?']


def getMessage(nick: str, game: str):
    num = randint(0, len(messages) - 1)
    print(num)
    message = messages[num]
    return message.replace('{0}', nick).replace('{1}', game)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    input = message.content

    if input.startswith('!h'):
        await message.channel.send(f'Command: d - Data, an - Add Nick, ag - Add Game')

    if input.startswith('!d'):
        await message.channel.send(nicks)
        await message.channel.send(games)
        await message.channel.send(data)

    if input.startswith('!an'):
        nicks.append(input.split(' ')[1])

    if input.startswith('!ag'):
        games.append(input.split(' ')[1])

@client.event
async def on_presence_update(prev, cur: discord.Member):
    if cur.activity == None:
        if cur.name:
            data[1] = False

        return

    nick = cur.name
    game = cur.activity.name

    print(f'{nick} - {game}')

    if nick in nicks and game in games:
        if data[1] == True:
            return

        channel = client.get_channel(942895908981473307)
        await channel.send(getMessage(nick, game))
        data[0] = nick
        data[1] = True

client.run('')
