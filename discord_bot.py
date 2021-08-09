#!/usr/bin/python3
from ERBSClient import ErbsClient
import discord
import random
from discord_bot_data import *

# instantiate the erbs api client
api_key_file = open('api-key')  # file containing one line of the ER:BS api key
private_api_key = api_key_file.readline().rstrip()
api_client = ErbsClient(api_key=private_api_key, version='v1')

# instantiate the discord bot
bot_token_file = open('discord-bot-token')  # file containing one line of the discord bot token
bot_token = bot_token_file.readline().rstrip()
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name=".rank <user> for ER:BS ranking"))

@client.event
async def on_message(message):
    content = message.content
    author = message.author
    channel = message.channel
    mentions = message.mentions

    # ignore message from bot itself
    if author == client.user:
        return
    # commands with constant responses
    elif content in COMMON_STRINGS_DICT:
        log_message(author, content)
        await channel.send(COMMON_STRINGS_DICT[content])
    # image URL of author or target's avatar
    elif content.startswith('.avatar'):
        log_message(author, content)
        if len(mentions) > 0:
            await channel.send(mentions[0].avatar_url)
        else:
            await channel.send(author.avatar_url)
    # ER:BS rank of user
    elif content.startswith('.rank '):
        log_message(author, content)
        embedVar = search_user_ranking(content.split()[1])
        await channel.send(embed=embedVar)
    # ER:BS games of user
    elif content.startswith('.games '):
        log_message(author, content)
        embedVar = search_user_games(content.split()[1])
        await channel.send(embed=embedVar)
    # skill information of ER:BS characters
    elif content.startswith('.info '):
        log_message(author, content)
        try:
            img = get_skill_information_image(content.split()[1], content.split()[2])
            await channel.send(file=img)
        except:
            await channel.send(COMMON_STRINGS_DICT['.info'])
    # roleplaying commands
    elif content.startswith(ROLEPLAYING_COMMANDS_TUP):
        log_message(author, content)
        command = content.lstrip('.')
        command = command.split()[0] if ' ' in command else command
        if len(mentions) > 0:
            embedVar = get_roleplay_image(command, author, mentions[0])
        else:
            embedVar = get_roleplay_image(command, author)
        try:
            await channel.send(embed=embedVar)
        except:
            await channel.send(COMMON_STRINGS_DICT['bad roleplaying command'])
    

def log_message(author, content):
    print(f'[+] {author}: {content}')


def search_user_ranking(nickname):
    if not nickname:
        return
    user_num = api_client.get_user_num(nickname)
    
    ranked_mmr = [0, 0, 0]
    normal_mmr = [0, 0, 0]
    
    # fetch and parse ranked game stats
    ranked_user_stats = api_client.get_user_stats(user_num, PRE_SEASON_3)
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
    embedVar.set_thumbnail(url=COMMON_STRINGS_DICT['bot avatar'])
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
    embedVar.set_thumbnail(url=COMMON_STRINGS_DICT['bot avatar'])
    
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
            game_type = 'Ranked (Season 2)'
        elif game_type == PRE_SEASON_3:
            game_type = 'Ranked (Pre-Season 3)'
        elif game_type == SEASON_3:
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
        
        embedVar.add_field(
            name='{0} {1}'.format(game_type, game_team_mode),
            value='{0}: rank #{1} - ({2}/{3}/{4})'.format(game_character, game_rank, game_kills, game_assists, game_monster_kills),
            inline=False
        )
    return embedVar


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
    # validate user input to prevent command injection
    if f'.{command}' not in ROLEPLAYING_COMMANDS_TUP:
        return None

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
    embedVar.set_image(url=image_url)
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


# start the discord bot
client.run(bot_token)