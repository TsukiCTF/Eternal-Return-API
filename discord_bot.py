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


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '!test':
        await message.channel.send('Hello')
    if message.content == '!rio':
        await message.channel.send('https://cdn.discordapp.com/attachments/414822020967301121/841097700384571402/rio.png')
    if message.content.startswith('!rank '):
        res = search_user_ranking(message.content.split()[1])
        await message.channel.send(res)
    if message.content.startswith('!exit'):
        exit()

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
        except IndexError:
            pass

    # parse ranked game stats
    for i in range(3):
        try:
            matching_team_mode = int(ranked_user_stats['userStats'][i]['matchingTeamMode'])
            ranked_mmr[matching_team_mode - 1] = ranked_user_stats['userStats'][i]['mmr']
        except IndexError:
            pass

    res = nickname + '\n'
    res += 'Normal Solo: {0}'.format(normal_mmr[0]) + '\n'
    res += 'Normal Duo: {0}'.format(normal_mmr[1]) + '\n'
    res += 'Normal Squad: {0}'.format(normal_mmr[2]) + '\n'
    res += 'Ranked Solo: {0}'.format(ranked_mmr[0]) + '\n'
    res += 'Ranked Duo: {0}'.format(ranked_mmr[1]) + '\n'
    res += 'Ranked Squad: {0}'.format(ranked_mmr[2]) + '\n'
    return res

# start the discord bot
client.run(bot_token)
