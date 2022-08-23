from random import seed
from random import randint
from time import sleep
import discord


intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
seed(1)

nick = ['uyuyuy']
game = ['Dota 2']
messages = ['@everyone , {0} goes {1}. Go with him! @PadoruPadoru espesially you!',
            '@everyone I ({0}) want to play {1}. Go? @PadoruPadoru espesially you!',
            '@everyone Go {1}? @PadoruPadoru',
            '@everyone Уебаный го {1}',
            '@everyone Пусички го {1}']


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
        await message.channel.send(f'Command: d - Data, st - Set Nick, sg - Set Game')

    if input.startswith('!d'):
        await message.channel.send(f'{nick[0]} - {game[0]}')

    if input.startswith('!sn'):
        nick[0] = input[4:]

    if input.startswith('!sg'):
        game[0] = input[4:]



@client.event
async def on_presence_update(prev: discord.Member, cur: discord.Member):
    if cur.activity == None:
        print('cur.activity == None')
        return

    if prev.activity != None and cur.activity.name == prev.activity.name:
        print('cur.activity.name == prev.activity.name')
        return

    if prev.activity != None:
        print(f'prev - {prev.name} - {prev.activity.name}')
    print(f'cur -  {cur.name} - {cur.activity.name}')
    print('-----')

    if nick[0] == cur.name and game[0] == cur.activity.name:
        channel = client.get_channel(942895908981473307)
        await channel.send(getMessage(cur.name, cur.activity.name))


client.run('')
