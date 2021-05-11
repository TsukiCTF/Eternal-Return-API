#!/usr/bin/python3
from ERBSClient import ErbsClient
import discord

# instantiate the erbs api client
api_key_file = open('api-key')  # file containing one line of the ER:BS api key
private_api_key = api_key_file.readline().rstrip()
api_client = ErbsClient(api_key=private_api_key, version='v1')

# instantiate the discord bot
bot_token_file = open('discord-bot-token')  # file containing one line of the discord bot token
bot_token = bot_token_file.readline().rstrip()
client = discord.Client()

# enum for tiers
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


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!'):
        print('[+]{0}: {1}'.format(message.author, message.content)) # log message
    if message.content == '!source':
        await message.channel.send('Author: Evade | Source code: https://github.com/TsukiCTF/Eternal-Return-API')
    if message.content == '!test':
        await message.channel.send('Hello')
    if message.content == '!rio':
        await message.channel.send('https://cdn.discordapp.com/attachments/414822020967301121/841097700384571402/rio.png')
    if message.content == '!shoichi':
        await message.channel.send('https://media.discordapp.net/attachments/395813565208068096/841529013625159690/viewimage.png')
    if message.content.startswith('!rank '):
        embedVar = search_user_ranking(message.content.split()[1])
        await message.channel.send(embed=embedVar)


def search_user_ranking(nickname):
    if not nickname:
        return
    user_num = api_client.get_user_num(nickname)
    # fetch normal, ranked game stats
    normal_user_stats = api_client.get_user_stats(user_num, 0)
    ranked_user_stats = api_client.get_user_stats(user_num, 3)

    # parse normal game stats
    normal_mmr = [0, 0, 0]
    ranked_mmr = [0, 0, 0]
    for i in range(3):
        try:
            matching_team_mode = int(normal_user_stats['userStats'][i]['matchingTeamMode'])
            normal_mmr[matching_team_mode - 1] = normal_user_stats['userStats'][i]['mmr']
        except:
            pass

    # parse ranked game stats
    for i in range(3):
        try:
            matching_team_mode = int(ranked_user_stats['userStats'][i]['matchingTeamMode'])
            ranked_mmr[matching_team_mode - 1] = ranked_user_stats['userStats'][i]['mmr']
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
    elif TITAN <= mmr:
        tier += 'Titan - {0} LP'.format(mmr % TITAN)
    return tier


# start the discord bot
client.run(bot_token)
