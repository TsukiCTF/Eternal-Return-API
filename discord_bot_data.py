# season constants
NORMAL_SEASON = 0
SEASON_1 = 1
PRE_SEASON_2 = 2
SEASON_2 = 3
PRE_SEASON_3 = 4
SEASON_3 = 5
PRE_SEASON_4 = 6
SEASON_4 = 7

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
    'Jan',
    'Eva',
    'Daniel',
    'Jenny',
    'Camilo',
    'Chloe',
    'Johann',
    'Bianca',
    'New Character'
]

# common string dictionary
COMMON_STRINGS_DICT = {
    '.help': '``.rank <name>`` : __search current ER:BS rank of user__\n' + \
            '``.games <name>`` : __search 10 most recent games of user__\n' + \
            '``.info <character name> <q/w/e/r/passive>`` : __get information of a character\'s skill__\n' + \
            '``.source`` : __link to source code of this bot__\n' + \
            '``.avatar`` : __image of profile picture__\n' + \
            '``.rio``, ``.fiora``, ``.rozzi``, etc. : __featured character images__\n' + \
            '``.tucc``, ``.bite``, ``.hug``, ``.dance``, ``.slap``, ``.poke``, ``.stare`` : __roleplaying commands__',
    '.source': 'Author: Evade | Source code: https://github.com/TsukiCTF/Eternal-Return-API',
    '.rio': '|| https://cdn.discordapp.com/attachments/414822020967301121/841097700384571402/rio.png ||',
    '.shoichi': 'https://cdn.discordapp.com/attachments/876628334933573664/912534529422532678/93677098_p1_master1200.jpg',
    '.adrianna': 'https://cdn.discordapp.com/attachments/837001169380573227/842264006790086676/maxresdefault.png',
    '.lenox': 'https://cdn.discordapp.com/attachments/818242488657117226/842263098564149249/image0.jpg',
    '.cathy': '|| https://cdn.discordapp.com/attachments/876628334933573664/912142057324306452/87937264_p0_master1200.jpg ||',
    '.nadine': 'https://cdn.discordapp.com/emojis/841500255614009384.png?v=1',
    '.isol': 'https://cdn.discordapp.com/attachments/817667857676632075/842401073775640586/viewimage.png',
    '.chiara': 'https://cdn.discordapp.com/attachments/844325341073113159/844325373129785364/cb38a4463de986eb5f39dfd725ffd22f.png',
    '.silvia': 'https://cdn.discordapp.com/attachments/835727238187057203/842281890705571880/85867309_p0_master1200.png',
    '.eva': 'https://cdn.discordapp.com/attachments/788518957953843222/850172838115541073/unknown.png',
    '.lidailin' : 'https://cdn.discordapp.com/attachments/841432452627038221/912383122656604170/86506149_p0_master1200.png',
    '.aya': 'https://cdn.discordapp.com/attachments/788518957953843222/912136943754674196/6b96934fa3abe1052a3fb945fd401c9c.jpg',
    '.hyejin': 'https://cdn.discordapp.com/attachments/788518957953843222/912136706415792128/viewimage.png',
    '.jackie': 'https://cdn.discordapp.com/attachments/788518957953843222/912136849856794684/EmJooe-VoAYd4a-.png',
    '.fiora': '|| https://cdn.discordapp.com/attachments/788518957953843222/912145330869518386/94161531_p0_master1200.jpg ||',
    '.rozzi': 'https://cdn.discordapp.com/attachments/788518957953843222/912136991842385950/viewimage.png',
    '.sua': 'https://cdn.discordapp.com/attachments/876628334933573664/912139981798125638/unknown.png',
    '.magnus': 'https://cdn.discordapp.com/attachments/788518957953843222/912143263081836554/89957942_p0_master1200.png',
    '.emma': 'https://cdn.discordapp.com/attachments/788518957953843222/912141347375415296/88353759_p0.png',
    '.jenny': 'https://cdn.discordapp.com/attachments/876628334933573664/912141413246984212/93459345_p0_master1200.jpg',
    '.adela': 'https://cdn.discordapp.com/attachments/912142102119469116/912142173263253574/87661714_p0_master1200.png',
    '.barbara': 'https://cdn.discordapp.com/attachments/788518957953843222/912142291706204241/t_pose_barb-1.png',
    '.nicky': 'https://cdn.discordapp.com/attachments/788518957953843222/912143368547606558/FAXdaaNVgAIb0Mm.png',
    '.luke': 'https://cdn.discordapp.com/attachments/876628334933573664/912143585149849630/unknown.png',
    '.nadja': 'https://cdn.discordapp.com/attachments/876628334933573664/912142057764683796/92511625_p0_master1200.jpg',
    '.hyunwoo': 'https://cdn.discordapp.com/attachments/788518957953843222/912150253711548486/download.png',
    '.hart': 'https://cdn.discordapp.com/attachments/788518957953843222/912143642888654868/E_bTQhxVcAED-oP.png',
    '.daniel': 'https://cdn.discordapp.com/attachments/788518957953843222/912143810845368370/91278952_p41_master1200.png',
    '.william': 'https://cdn.discordapp.com/attachments/788518957953843222/912143951274860574/91569318_p0_master1200.png',
    '.sissela': 'https://cdn.discordapp.com/attachments/788518957953843222/912144093600153640/viewimage.png',
    '.eleven': 'https://cdn.discordapp.com/attachments/788518957953843222/912144214442246156/viewimage.png',
    '.nathapon': 'https://cdn.discordapp.com/attachments/788518957953843222/912144458550751242/image0.png',
    '.wickline': 'https://cdn.discordapp.com/attachments/788518957953843222/912145036236427264/90618354_p0_master1200.jpg',
    '.alex': 'https://cdn.discordapp.com/attachments/788518957953843222/912145412943663134/Alex.png',
    '.aiden': 'https://cdn.discordapp.com/attachments/788518957953843222/912145303933714472/Untitled_Artwork.png',
    '.pokimane': 'https://c.tenor.com/rtnshG9YFykAAAAM/rick-astley-rick-roll.gif',
    '.yuki': 'https://pbs.twimg.com/media/FD1S4bracAAgNbb.jpg:large',
    '.aesop': 'https://cdn.discordapp.com/attachments/788518957953843222/912148397555859456/5120.png',
    '.zahir': 'https://cdn.discordapp.com/emojis/883182165922291743.gif?size=128',
    '.johann': 'https://cdn.discordapp.com/attachments/788518957953843222/912137201402392586/viewimage.png',
    '.bernice': 'https://cdn.discordapp.com/attachments/788518957953843222/912149393245884436/unknown.png',
    '.camilio': 'https://cdn.discordapp.com/attachments/788518957953843222/912149951813943337/unknown.png',
    '.xiukai': 'https://cdn.discordapp.com/attachments/788518957953843222/912149887230042132/9k.png',
    '.info': 'Use: ``.info <character name> <q/w/e/r/passive>``',
    'bad roleplaying command': 'No such roleplaying command exists. Use ``.help`` to list available commands',
    'bot avatar': 'https://media.discordapp.net/attachments/395813565208068096/841530242074148894/rio.png'
}

# roleplaying command tuple
ROLEPLAYING_COMMANDS_TUP = (
    '.bite', '.hug', '.dance', '.slap', '.poke', '.stare', '.tucc'
)
