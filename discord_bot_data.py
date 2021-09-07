# season constants
NORMAL_SEASON = 0
SEASON_1 = 1
PRE_SEASON_2 = 2
SEASON_2 = 3
PRE_SEASON_3 = 4
SEASON_3 = 5

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
    'Nathapon',
    'Nicky',
    'Jan',
    'Eva',
    'Daniel',
    'New Character'
]

# common string dictionary
COMMON_STRINGS_DICT = {
    '.help': '``.rank <name>`` : __search current ER:BS rank of user__\n' + \
            '``.games <name>`` : __search 10 most recent games of user__\n' + \
            '``.info <character name> <q/w/e/r/passive>`` : __get information of a character\'s skill__\n' + \
            '``.source`` : __link to source code of this bot__\n' + \
            '``.avatar`` : __image of profile picture__\n' + \
            '``.rio``, ``.shoichi``, ``.adrianna``, ``.lenox``, ``.cathy``, ``.nadine``, ``.isol``, ``.chiara``, ``.silvia``, ``.eva`` : __featured character images__\n' + \
            '``.tucc``, ``.bite``, ``.hug``, ``.dance``, ``.slap``, ``.poke``, ``.stare`` : __roleplaying commands__',
    '.source': 'Author: Evade | Source code: https://github.com/TsukiCTF/Eternal-Return-API',
    '.rio': 'Preview Disabled: <https://cdn.discordapp.com/attachments/414822020967301121/841097700384571402/rio.png>',
    '.shoichi': 'https://cdn.discordapp.com/attachments/818242488657117226/841544863627083776/image0.jpg',
    '.adrianna': 'https://cdn.discordapp.com/attachments/837001169380573227/842264006790086676/maxresdefault.png',
    '.lenox': 'https://cdn.discordapp.com/attachments/818242488657117226/842263098564149249/image0.jpg',
    '.cathy': 'https://cdn.discordapp.com/emojis/840598438797115392.png?v=1',
    '.nadine': 'https://cdn.discordapp.com/emojis/841500255614009384.png?v=1',
    '.isol': 'https://cdn.discordapp.com/attachments/817667857676632075/842401073775640586/viewimage.png',
    '.chiara': 'https://cdn.discordapp.com/attachments/844325341073113159/844325373129785364/cb38a4463de986eb5f39dfd725ffd22f.png',
    '.silvia': 'https://cdn.discordapp.com/attachments/835727238187057203/842281890705571880/85867309_p0_master1200.png',
    '.eva': 'https://cdn.discordapp.com/attachments/788518957953843222/850172838115541073/unknown.png',
    '.info': 'Use: ``.info <character name> <q/w/e/r/passive>``',
    'bad roleplaying command': 'No such roleplaying command exists. Use ``.help`` to list available commands',
    'bot avatar': 'https://media.discordapp.net/attachments/395813565208068096/841530242074148894/rio.png'
}

# roleplaying command tuple
ROLEPLAYING_COMMANDS_TUP = (
    '.bite', '.hug', '.dance', '.slap', '.poke', '.stare', '.tucc'
)
