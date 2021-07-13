#!/usr/bin/python3
from ERBSClient import ErbsClient
import discord
import random

# instantiate the erbs api client
api_key_file = open('api-key')  # file containing one line of the ER:BS api key
private_api_key = api_key_file.readline().rstrip()
api_client = ErbsClient(api_key=private_api_key, version='v1')

# instantiate the discord bot
bot_token_file = open('discord-bot-token')  # file containing one line of the discord bot token
bot_token = bot_token_file.readline().rstrip()
client = discord.Client()


# season constants
NORMAL_SEASON = 0
SEASON_1 = 1
PRE_SEASON_2 = 2
SEASON_2 = 3

# mode constants
SOLO_MODE = 1
DUO_MODE = 2
SQUAD_MODE = 3

# tier constants
IRON_4 = 0
IRON_3 = 100
IRON_2 = 200
IRON_1 = 300
BRONZE_4 = 400
BRONZE_3 = 500
BRONZE_2 = 600
BRONZE_1 = 700
SILVER_4 = 800
SILVER_3 = 900
SILVER_2 = 1000
SILVER_1 = 1100
GOLD_4 = 1200
GOLD_3 = 1300
GOLD_2 = 1400
GOLD_1 = 1500
PLATINUM_4 = 1600
PLATINUM_3 = 1700
PLATINUM_2 = 1800
PLATINUM_1 = 1900
DIAMOND_4 = 2000
DIAMOND_3 = 2100
DIAMOND_2 = 2200
DIAMOND_1 = 2300
TITAN = 2400
IMMORTAL = 2600

# character name list
CHARACTER_LIST = [
    'null', 
    'Jackie',
    'Aya',
    'Fiora',
    'Magnus',
    'Zahir',
    'Nadine',
    'Hyunwoo',
    'Hart',
    'Isol',
    'LiDailin',
    'Yuki',
    'Hyejin',
    'Xiukai',
    'Chiara',
    'Sissela',
    'Silvia',
    'Adriana',
    'Shoichi',
    'Emma',
    'Lenox',
    'Rozzi',
    'Luke',
    'Cathy',
    'Adela',
    'Bernice',
    'Barbara',
    'Alex',
    'Sua',
    'Leon',
    'Eleven',
    'Rio',
    'William',
    'Nicky',
    'New Character']



@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name=".rank <user> for ER:BS ranking"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content == '.help':
        print(f'[+]{message.author}: {message.content}')
        await message.channel.send('``.rank <name>`` : __search current ER:BS rank of user__\n' + \
            '``.games <name>`` : __search 10 most recent games of user__\n' + \
            '``.info <character name> <q/w/e/r/passive>`` : __get information of a character\'s skill__\n' + \
            '``.source`` : __link to source code of this bot__\n' + \
            '``.rio``, ``.shoichi``, ``.adrianna``, ``.lenox``, ``.cathy``, ``.nadine``, ``.isol``, ``.chiara``, ``.silvia``, ``.eva`` : __featured character images__\n' + \
            '``.bite``, ``.hug``, ``.dance``, ``.slap``, ``.poke``, ``.stare`` : __roleplaying commands__')
    elif message.content == '.source':
        print(f'[+]{message.author}: {message.content}')
        await message.channel.send('Author: Evade | Source code: https://github.com/TsukiCTF/Eternal-Return-API')
    elif message.content == '.rio':
        print(f'[+]{message.author}: {message.content}')
        await message.channel.send('Preview Disabled: <https://cdn.discordapp.com/attachments/414822020967301121/841097700384571402/rio.png>')
    elif message.content == '.shoichi':
        print(f'[+]{message.author}: {message.content}')
        await message.channel.send('https://cdn.discordapp.com/attachments/818242488657117226/841544863627083776/image0.jpg')
    elif message.content == '.adrianna':
        print(f'[+]{message.author}: {message.content}')
        await message.channel.send('https://cdn.discordapp.com/attachments/837001169380573227/842264006790086676/maxresdefault.png')
    elif message.content == '.lenox':
        print(f'[+]{message.author}: {message.content}')
        await message.channel.send('https://cdn.discordapp.com/attachments/818242488657117226/842263098564149249/image0.jpg')
    elif message.content == '.cathy':
        print(f'[+]{message.author}: {message.content}')
        await message.channel.send('https://cdn.discordapp.com/emojis/840598438797115392.png?v=1')
    elif message.content == '.nadine':
        print(f'[+]{message.author}: {message.content}')
        await message.channel.send('https://cdn.discordapp.com/emojis/841500255614009384.png?v=1')
    elif message.content == '.isol':
        print(f'[+]{message.author}: {message.content}')
        await message.channel.send('https://cdn.discordapp.com/attachments/817667857676632075/842401073775640586/viewimage.png')
    elif message.content == '.chiara':
        print(f'[+]{message.author}: {message.content}')
        await message.channel.send('https://cdn.discordapp.com/attachments/844325341073113159/844325373129785364/cb38a4463de986eb5f39dfd725ffd22f.png')
    elif message.content == '.silvia':
        print(f'[+]{message.author}: {message.content}')
        await message.channel.send('https://cdn.discordapp.com/attachments/835727238187057203/842281890705571880/85867309_p0_master1200.png')
    elif message.content == '.eva':
        print(f'[+]{message.author}: {message.content}')
        await message.channel.send('https://cdn.discordapp.com/attachments/788518957953843222/850172838115541073/unknown.png')
    elif message.content.startswith('.avatar'):
        print(f'[+]{message.author}: {message.content}')
        if message.mentions.__len__() > 0:
            await message.channel.send(message.mentions[0].avatar_url)
        else:
            await message.channel.send(message.author.avatar_url)
    elif message.content.startswith('.rank '):
        print(f'[+]{message.author}: {message.content}')
        embedVar = search_user_ranking(message.content.split()[1])
        await message.channel.send(embed=embedVar)
    elif message.content.startswith('.games '):
        print(f'[+]{message.author}: {message.content}')
        embedVar = search_user_games(message.content.split()[1])
        await message.channel.send(embed=embedVar)
    elif message.content.startswith('.info '):
        print(f'[+]{message.author}: {message.content}')
        try:
            img = get_skill_information_image(message.content.split()[1], message.content.split()[2])
            await message.channel.send(file=img)
        except:
            await message.channel.send('Use: ``.info <character name> <q/w/e/r/passive>``')
    elif message.content.startswith('.bite'):
        print(f'[+]{message.author}: {message.content}')
        if message.mentions.__len__() > 0:
            embedVar = get_roleplay_image('bite', message.author, message.mentions[0])
        else:
            embedVar = get_roleplay_image('bite', message.author)
        await message.channel.send(embed=embedVar)
    elif message.content.startswith('.hug'):
        print(f'[+]{message.author}: {message.content}')
        if message.mentions.__len__() > 0:
            embedVar = get_roleplay_image('hug', message.author, message.mentions[0])
        else:
            embedVar = get_roleplay_image('hug', message.author)
        await message.channel.send(embed=embedVar)
    elif message.content.startswith('.dance'):
        print(f'[+]{message.author}: {message.content}')
        if message.mentions.__len__() > 0:
            embedVar = get_roleplay_image('dance', message.author, message.mentions[0])
        else:
            embedVar = get_roleplay_image('dance', message.author)
        await message.channel.send(embed=embedVar)
    elif message.content.startswith('.slap'):
        print(f'[+]{message.author}: {message.content}')
        if message.mentions.__len__() > 0:
            embedVar = get_roleplay_image('slap', message.author, message.mentions[0])
        else:
            embedVar = get_roleplay_image('slap', message.author)
        await message.channel.send(embed=embedVar)
    elif message.content.startswith('.poke'):
        print(f'[+]{message.author}: {message.content}')
        if message.mentions.__len__() > 0:
            embedVar = get_roleplay_image('poke', message.author, message.mentions[0])
        else:
            embedVar = get_roleplay_image('poke', message.author)
        await message.channel.send(embed=embedVar)
    elif message.content.startswith('.stare'):
        print(f'[+]{message.author}: {message.content}')
        if message.mentions.__len__() > 0:
            embedVar = get_roleplay_image('stare', message.author, message.mentions[0])
        else:
            embedVar = get_roleplay_image('stare', message.author)
        await message.channel.send(embed=embedVar)


def search_user_ranking(nickname):
    if not nickname:
        return
    user_num = api_client.get_user_num(nickname)
    
    ranked_mmr = [0, 0, 0]
    normal_mmr = [0, 0, 0]
    
    # fetch and parse ranked game stats
    ranked_user_stats = api_client.get_user_stats(user_num, SEASON_2)
    for i in range(3):
        try:
            matching_team_mode = int(ranked_user_stats['userStats'][i]['matchingTeamMode'])
            ranked_mmr[matching_team_mode - 1] = ranked_user_stats['userStats'][i]['mmr']
        except:
            pass
    
    # fetch and parse normal game stats
    normal_user_stats = api_client.get_user_stats(user_num, NORMAL_SEASON)
    for i in range(3):
        try:
            matching_team_mode = int(normal_user_stats['userStats'][i]['matchingTeamMode'])
            normal_mmr[matching_team_mode - 1] = normal_user_stats['userStats'][i]['mmr']
        except:
            pass

    embedVar = discord.Embed(title=nickname.upper(), color=0x0db6e0)
    embedVar.set_thumbnail(url='https://media.discordapp.net/attachments/395813565208068096/841530242074148894/rio.png')
    embedVar.add_field(name='Season 2 Solo', value=get_tier(ranked_mmr[0]), inline=True)
    embedVar.add_field(name='Duo', value=get_tier(ranked_mmr[1]), inline=True)
    embedVar.add_field(name='Squad', value=get_tier(ranked_mmr[2]), inline=True)
    embedVar.add_field(name='Normal Solo', value='{0} MMR'.format(normal_mmr[0]), inline=True)
    embedVar.add_field(name='Duo', value='{0} MMR'.format(normal_mmr[1]), inline=True)
    embedVar.add_field(name='Squad', value='{0} MMR'.format(normal_mmr[2]), inline=True)
    return embedVar

    
def search_user_games(nickname):
    if not nickname:
        return
    user_num = api_client.get_user_num(nickname)
    
    # fetch and parse user games
    user_games_unparsed = api_client.get_user_games(user_num)
    user_games = user_games_unparsed['userGames']
    
    embedVar = discord.Embed(title='10 Recent Games for {0}'.format(nickname.upper()), color=0x0db6e0)
    embedVar.set_thumbnail(url='https://media.discordapp.net/attachments/395813565208068096/841530242074148894/rio.png')
    
    for game in user_games:
        # check game season
        game_type = int(game['seasonId'])
        if game_type == NORMAL_SEASON:
            game_type = 'Normal'
        elif game_type == SEASON_1:
            game_type = 'Ranked (Season 1)'
        elif game_type == PRE_SEASON_2:
            game_type = 'Ranked (Pre-Season 2)'
        elif game_type == SEASON_2:
            game_type = 'Ranked'
        
        # check game mode
        game_team_mode = int(game['matchingTeamMode'])
        if game_team_mode == SOLO_MODE:
            game_team_mode = 'Solo'
        elif game_team_mode == DUO_MODE:
            game_team_mode = 'Duo'
        elif game_team_mode == SQUAD_MODE:
            game_team_mode = 'Squad'
        
        # check game rank
        game_rank = int(game['gameRank'])
        
        # check game kills, assists, monster kills
        game_kills = int(game['playerKill'])
        game_assists = int(game['playerAssistant'])
        game_monster_kills = int(game['monsterKill']) 
        
        # check game character
        game_character = CHARACTER_LIST[int(game['characterNum'])]
        
        embedVar.add_field(name='{0} {1}'.format(game_type, game_team_mode), value='{0}: rank #{1} - ({2}/{3}/{4})'.format(game_character, game_rank, game_kills, game_assists, game_monster_kills), inline=False)
      
    return embedVar


def get_tier(mmr):
    tier = ''
    if mmr == 0:
        tier += 'Unranked'
    elif IRON_4 < mmr < IRON_3:
        tier += 'Iron 4 - {0} LP'.format(mmr % IRON_4)
    elif IRON_3 <= mmr < IRON_2:
        tier += 'Iron 3 - {0} LP'.format(mmr % IRON_3)
    elif IRON_2 <= mmr < IRON_1:
        tier += 'Iron 2 - {0} LP'.format(mmr % IRON_2)
    elif IRON_1 <= mmr < BRONZE_4:
        tier += 'Iron 1 - {0} LP'.format(mmr % IRON_1)
    elif BRONZE_4 <= mmr < BRONZE_3:
        tier += 'Bronze 4 - {0} LP'.format(mmr % BRONZE_4)
    elif BRONZE_3 <= mmr < BRONZE_2:
        tier += 'Bronze 3 - {0} LP'.format(mmr % BRONZE_3)
    elif BRONZE_2 <= mmr < BRONZE_1:
        tier += 'Bronze 2 - {0} LP'.format(mmr % BRONZE_2)
    elif BRONZE_1 <= mmr < SILVER_4:
        tier += 'Bronze 1 - {0} LP'.format(mmr % BRONZE_1)
    elif SILVER_4 <= mmr < SILVER_3:
        tier += 'Silver 4 - {0} LP'.format(mmr % SILVER_4)
    elif SILVER_3 <= mmr < SILVER_2:
        tier += 'Silver 3 - {0} LP'.format(mmr % SILVER_3)
    elif SILVER_2 <= mmr < SILVER_1:
        tier += 'Silver 2 - {0} LP'.format(mmr % SILVER_2)
    elif SILVER_1 <= mmr < GOLD_4:
        tier += 'Silver 1 - {0} LP'.format(mmr % SILVER_1)
    elif GOLD_4 <= mmr < GOLD_3:
        tier += 'Gold 4 - {0} LP'.format(mmr % GOLD_4)
    elif GOLD_3 <= mmr < GOLD_2:
        tier += 'Gold 3 - {0} LP'.format(mmr % GOLD_3)
    elif GOLD_2 <= mmr < GOLD_1:
        tier += 'Gold 2 - {0} LP'.format(mmr % GOLD_2)
    elif GOLD_1 <= mmr < PLATINUM_4:
        tier += 'Gold 1 - {0} LP'.format(mmr % GOLD_1)
    elif PLATINUM_4 <= mmr < PLATINUM_3:
        tier += 'Platinum 4 - {0} LP'.format(mmr % PLATINUM_4)
    elif PLATINUM_3 <= mmr < PLATINUM_2:
        tier += 'Platinum 3 - {0} LP'.format(mmr % PLATINUM_3)
    elif PLATINUM_2 <= mmr < PLATINUM_1:
        tier += 'Platinum 2 - {0} LP'.format(mmr % PLATINUM_2)
    elif PLATINUM_1 <= mmr < DIAMOND_4:
        tier += 'Platinum 1 - {0} LP'.format(mmr % PLATINUM_1)
    elif DIAMOND_4 <= mmr < DIAMOND_3:
        tier += 'Diamond 4 - {0} LP'.format(mmr % DIAMOND_4)
    elif DIAMOND_3 <= mmr < DIAMOND_2:
        tier += 'Diamond 3 - {0} LP'.format(mmr % DIAMOND_3)
    elif DIAMOND_2 <= mmr < DIAMOND_1:
        tier += 'Diamond 2 - {0} LP'.format(mmr % DIAMOND_2)
    elif DIAMOND_1 <= mmr < TITAN:
        tier += 'Diamond 1 - {0} LP'.format(mmr % DIAMOND_1)
    elif TITAN <= mmr < IMMORTAL:
        tier += 'Titan - {0} LP'.format(mmr % TITAN)
    elif IMMORTAL <= mmr:
        tier += 'Immortal - {0} LP'.format(mmr % IMMORTAL)
    return tier


def get_skill_information_image(character_name, skill_name):
    character_name = character_name.lower()
    skill_name = skill_name.lower()
    
    # validate user input to prevent command injection
    if not character_name.isalpha():
        return None
    if not skill_name.isalpha():
        return None
        
    image_path = f'resource/{character_name}/{skill_name}.png'
    image = None
    with open(image_path, 'rb') as f:
        image = discord.File(f)
    return image


def get_roleplay_image(command, author, mention=None):
    # open text file containing URLs for command
    text_file_path = f'resource/roleplay/{command}.txt'
    with open(text_file_path, 'r') as f:
        lines = f.readlines()
        # choose a random URL
        image_url = random.choice(lines)
    
    # set description text
    if (mention == None):
        author = str(author).split('#')[0]   # strip discord tag
        description_text = f'**{author}** {command}s...'
    else:
        author = str(author).split('#')[0]   # strip discord tag
        mention = str(mention).split('#')[0]
        description_text = f'**{author}** {command}s **{mention}**...'

    embedVar = discord.Embed(description=description_text, color=0x0db6e0)
    embedVar.set_thumbnail(url=image_url)
    return embedVar


# start the discord bot
client.run(bot_token)