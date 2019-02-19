import math
from operator import itemgetter
import random

ARI = [['WAS',31,'H'],['LAR',17,'A'],['CHI',5,'H'],['SEA',27,'H'],['SF',28,'A'],['MIN',19,'A'],['DEN',9,'H'],['SF',28,'H'],['B','Y','E','W','E','E','K'],['KC',15,'A'],['OAK',24,'H'],['LAC',16,'A'],['GB',11,'A'],['DET',10,'H'],['ATL',1,'A'],['LAR',17,'H'],['SEA',27,'A']]
ATL = [['PHI',25,'A'],['CAR',4,'H'],['NO',21,'H'],['CIN',6,'H'],['PIT',26,'A'],['TB',29,'H'],['NYG',22,'H'],['B','Y','E','W','E','E','K'],['WAS',31,'A'],['CLE',7,'A'],['DAL',8,'H'],['NO',21,'A'],['BAL',2,'H'],['GB',11,'A'],['ARI',0,'H'],['CAR',4,'A'],['TB',29,'A']]
BAL = [['BUF',3,'H'],['CIN',6,'A'],['DEN',9,'H'],['PIT',26,'A'],['CLE',7,'A'],['TEN',30,'A'],['NO',21,'H'],['CAR',4,'A'],['PIT',26,'H'],['B','Y','E','W','E','E','K'],['CIN',6,'H'],['OAK',24,'H'],['ATL',1,'A'],['KC',15,'A'],['TB',29,'H'],['LAC',16,'A'],['CLE',7,'H']]
BUF = [['BAL',2,'A'],['LAC',16,'H'],['MIN',19,'A'],['GB',11,'A'],['TEN',30,'H'],['HOU',12,'A'],['IND',13,'A'],['NE',20,'H'],['CHI',5,'H'],['NYJ',23,'A'],['B','Y','E','W','E','E','K'],['JAX',14,'H'],['MIA',18,'A'],['NYJ',23,'H'],['DET',10,'H'],['NE',20,'A'],['MIA',18,'H']]
CAR = [['DAL',8,'H'],['ATL',1,'A'],['CIN',6,'H'],['B','Y','E','W','E','E','K'],['NYG',22,'H'],['WAS',31,'A'],['PHI',25,'A'],['BAL',2,'H'],['TB',29,'H'],['PIT',26,'A'],['DET',10,'A'],['SEA',27,'H'],['TB',29,'A'],['CLE',7,'A'],['NO',21,'H'],['ATL',1,'H'],['NO',21,'A']]
CHI = [['GB',11,'A'],['SEA',27,'H'],['ARI',0,'A'],['TB',29,'H'],['B','Y','E','W','E','E','K'],['MIA',18,'A'],['NE',20,'H'],['NYJ',23,'H'],['BUF',3,'A'],['DET',10,'H'],['MIN',19,'H'],['DET',10,'A'],['NYG',22,'A'],['LAR',17,'H'],['GB',11,'H'],['SF',28,'A'],['MIN',19,'A']]
CIN = [['IND',13,'A'],['BAL',2,'H'],['CAR',4,'A'],['ATL',1,'A'],['MIA',18,'H'],['PIT',26,'H'],['KC',15,'A'],['TB',29,'H'],['B','Y','E','W','E','E','K'],['NO',21,'H'],['BAL',2,'A'],['CLE',7,'H'],['DEN',9,'H'],['LAC',16,'A'],['OAK',24,'H'],['CLE',7,'A'],['PIT',26,'A']]
CLE = [['PIT',26,'H'],['NO',21,'A'],['NYJ',23,'H'],['OAK',24,'A'],['BAL',2,'H'],['LAC',16,'H'],['TB',29,'A'],['PIT',26,'A'],['KC',15,'H'],['ATL',1,'H'],['B','Y','E','W','E','E','K'],['CIN',6,'A'],['HOU',12,'A'],['CAR',4,'H'],['DEN',9,'A'],['CIN',6,'H'],['BAL',2,'A']]
DAL = [['CAR',4,'A'],['NYG',22,'H'],['SEA',27,'A'],['DET',10,'H'],['HOU',12,'A'],['JAX',14,'H'],['WAS',31,'A'],['B','Y','E','W','E','E','K'],['TEN',30,'H'],['PHI',25,'A'],['ATL',1,'A'],['WAS',31,'H'],['NO',21,'H'],['PHI',25,'H'],['IND',13,'A'],['TB',29,'H'],['NYG',22,'A']]
DEN = [['SEA',27,'H'],['OAK',24,'H'],['BAL',2,'A'],['KC',15,'H'],['NYJ',23,'A'],['LAR',17,'H'],['ARI',0,'A'],['KC',15,'A'],['HOU',12,'H'],['B','Y','E','W','E','E','K'],['LAC',16,'A'],['PIT',26,'H'],['CIN',6,'A'],['SF',28,'A'],['CLE',7,'H'],['OAK',24,'A'],['LAC',16,'H']]
DET = [['NYJ',23,'H'],['SF',28,'A'],['NE',20,'H'],['DAL',8,'A'],['GB',11,'H'],['B','Y','E','W','E','E','K'],['MIA',18,'A'],['SEA',27,'H'],['MIN',19,'A'],['CHI',5,'A'],['CAR',4,'H'],['CHI',5,'H'],['LAR',17,'H'],['ARI',0,'A'],['BUF',3,'A'],['MIN',19,'H'],['GB',11,'A']]
GB = [['CHI',5,'H'],['MIN',19,'H'],['WAS',31,'A'],['BUF',3,'H'],['DET',10,'A'],['SF',28,'H'],['B','Y','E','W','E','E','K'],['LAR',17,'A'],['NE',20,'A'],['MIA',18,'H'],['SEA',27,'A'],['MIN',19,'A'],['ARI',0,'H'],['ATL',1,'H'],['CHI',5,'A'],['NYJ',23,'A'],['DET',10,'H']]
HOU = [['NE',20,'A'],['TEN',30,'A'],['NYG',22,'H'],['IND',13,'A'],['DAL',8,'H'],['BUF',3,'H'],['JAX',14,'A'],['MIA',18,'H'],['DEN',9,'A'],['B','Y','E','W','E','E','K'],['WAS',31,'A'],['TEN',30,'H'],['CLE',7,'H'],['IND',13,'H'],['NYJ',23,'A'],['PHI',25,'A'],['JAX',14,'H']]
IND = [['CIN',6,'H'],['WAS',31,'A'],['PHI',25,'A'],['HOU',12,'H'],['NE',20,'A'],['NYJ',23,'A'],['BUF',3,'H'],['OAK',24,'A'],['B','Y','E','W','E','E','K'],['JAX',14,'H'],['TEN',30,'H'],['MIA',18,'H'],['JAX',14,'A'],['HOU',12,'A'],['DAL',8,'H'],['NYG',22,'H'],['TEN',30,'A']]
JAX = [['NYG',22,'A'],['NE',20,'H'],['TEN',30,'H'],['NYJ',23,'H'],['KC',15,'A'],['DAL',8,'A'],['HOU',12,'H'],['PHI',25,'H'],['B','Y','E','W','E','E','K'],['IND',13,'A'],['PIT',26,'H'],['BUF',5,'A'],['IND',13,'H'],['TEN',30,'A'],['WAS',31,'H'],['MIA',18,'A'],['HOU',12,'A']]
KC = [['LAC',16,'A'],['PIT',26,'A'],['SF',28,'H'],['DEN',9,'A'],['JAX',14,'H'],['NE',20,'A'],['CIN',6,'H'],['DEN',9,'H'],['CLE',7,'A'],['ARI',0,'H'],['LAR',17,'A'],['B','Y','E','W','E','E','K'],['OAK',24,'A'],['BAL',2,'H'],['LAC',16,'H'],['SEA',27,'A'],['OAK',24,'H']]
LAC = [['KC',15,'H'],['BUF',3,'A'],['LAR',17,'A'],['SF',28,'H'],['OAK',24,'H'],['CLE',7,'A'],['TEN',30,'H'],['B','Y','E','W','E','E','K'],['SEA',27,'A'],['OAK',24,'A'],['DEN',9,'H'],['ARI',0,'H'],['PIT',26,'A'],['CIN',6,'H'],['KC',15,'A'],['BAL',2,'H'],['DEN',9,'A']]
LAR = [['OAK',24,'A'],['ARI',0,'H'],['LAC',16,'H'],['MIN',19,'H'],['SEA',27,'A'],['DEN',9,'A'],['SF',28,'A'],['GB',11,'H'],['NO',21,'A'],['SEA',27,'H'],['KC',15,'H'],['B','Y','E','W','E','E','K'],['DET',10,'A'],['CHI',5,'A'],['PHI',25,'H'],['ARI',0,'A'],['SF',28,'H']]
MIA = [['TEN',30,'H'],['NYJ',23,'A'],['OAK',24,'H'],['NE',20,'A'],['CIN',6,'A'],['CHI',5,'H'],['DET',10,'H'],['HOU',12,'A'],['NYJ',23,'H'],['GB',11,'A'],['B','Y','E','W','E','E','K'],['IND',13,'A'],['BUF',3,'H'],['NE',20,'H'],['MIN',19,'A'],['JAX',14,'H'],['BUF',3,'A']]
MIN = [['SF',28,'H'],['GB',11,'A'],['BUF',3,'H'],['LAR',17,'A'],['PHI',25,'A'],['ARI',0,'H'],['NYJ',23,'A'],['NO',21,'H'],['DET',10,'H'],['B','Y','E','W','E','E','K'],['CHI',5,'A'],['GB',11,'H'],['NE',20,'A'],['SEA',27,'A'],['MIA',18,'H'],['DET',10,'A'],['CHI',5,'H']]
NE = [['HOU',12,'H'],['JAX',14,'A'],['DET',10,'A'],['MIA',18,'H'],['IND',13,'H'],['KC',15,'H'],['CHI',5,'A'],['BUF',3,'A'],['GB',11,'H'],['TEN',30,'A'],['B','Y','E','W','E','E','K'],['NYJ',23,'A'],['MIN',19,'H'],['MIA',18,'A'],['PIT',26,'A'],['BUF',3,'H'],['NYJ',23,'H']]
NO = [['TB',29,'H'],['CLE',7,'H'],['ATL',1,'A'],['NYG',22,'A'],['WAS',31,'H'],['B','Y','E','W','E','E','K'],['BAL',2,'A'],['MIN',19,'A'],['LAR',17,'H'],['CIN',6,'A'],['PHI',25,'H'],['ATL',1,'H'],['DAL',8,'A'],['TB',29,'A'],['CAR',4,'A'],['PIT',26,'H'],['CAR',4,'H']]
NYG = [['JAX',14,'H'],['DAL',8,'A'],['HOU',12,'A'],['NO',21,'H'],['CAR',4,'A'],['PHI',25,'H'],['ATL',1,'A'],['WAS',31,'H'],['B','Y','E','W','E','E','K'],['SF',28,'A'],['TB',29,'H'],['PHI',25,'A'],['CHI',5,'H'],['WAS',31,'A'],['TEN',30,'H'],['IND',13,'A'],['DAL',8,'H']]
NYJ = [['DET',10,'A'],['MIA',18,'H'],['CLE',7,'A'],['JAX',14,'A'],['DEN',9,'H'],['IND',13,'H'],['MIN',19,'H'],['CHI',5,'A'],['MIA',18,'A'],['BUF',3,'H'],['B','Y','E','W','E','E','K'],['NE',20,'H'],['TEN',30,'A'],['BUF',3,'A'],['HOU',12,'H'],['GB',11,'H'],['NE',20,'A']]
OAK = [['LAR',17,'H'],['DEN',9,'A'],['MIA',18,'A'],['CLE',7,'H'],['LAC',16,'A'],['SEA',27,'H'],['B','Y','E','W','E','E','K'],['IND',13,'H'],['SF',28,'A'],['LAC',16,'H'],['ARI',0,'A'],['BAL',2,'A'],['KC',15,'H'],['PIT',26,'H'],['CIN',6,'A'],['DEN',9,'H'],['KC',15,'A']]
PHI = [['ATL',1,'H'],['TB',29,'A'],['IND',13,'H'],['TEN',30,'A'],['MIN',19,'H'],['NYG',22,'A'],['CAR',4,'H'],['JAX',14,'A'],['B','Y','E','W','E','E','K'],['DAL',8,'H'],['NO',21,'A'],['NYG',22,'H'],['WAS',31,'H'],['DAL',8,'A'],['LAR',17,'A'],['HOU',12,'H'],['WAS',31,'A']]
PIT = [['CLE',7,'A'],['KC',15,'H'],['TB',29,'A'],['BAL',2,'H'],['ATL',1,'H'],['CIN',6,'A'],['B','Y','E','W','E','E','K'],['CLE',7,'H'],['BAL',2,'A'],['CAR',4,'H'],['JAX',14,'A'],['DEN',9,'A'],['LAC',16,'H'],['OAK',24,'A'],['NE',20,'H'],['NO',21,'A'],['CIN',6,'H']]
SEA = [['DEN',9,'A'],['CHI',5,'A'],['DAL',8,'H'],['ARI',0,'A'],['LAR',17,'H'],['OAK',24,'A'],['B','Y','E','W','E','E','K'],['DET',10,'A'],['LAC',16,'H'],['LAR',17,'A'],['GB',11,'H'],['CAR',4,'A'],['SF',28,'H'],['MIN',19,'H'],['SF',28,'A'],['KC',15,'H'],['ARI',0,'A']]
SF = [['MIN',19,'A'],['DET',10,'H'],['KC',15,'A'],['LAC',16,'A'],['ARI',0,'H'],['GB',11,'A'],['LAR',17,'H'],['ARI',0,'A'],['OAK',24,'H'],['NYG',22,'H'],['B','Y','E','W','E','E','K'],['TB',29,'A'],['SEA',27,'A'],['DEN',9,'H'],['SEA',27,'H'],['CHI',5,'H'],['LAR',17,'A']]
TB = [['NO',21,'A'],['PHI',25,'H'],['PIT',26,'H'],['CHI',5,'A'],['B','Y','E','W','E','E','K'],['ATL',1,'A'],['CLE',7,'H'],['CIN',6,'A'],['CAR',4,'A'],['WAS',31,'H'],['NYG',22,'A'],['SF',28,'H'],['CAR',4,'H'],['NO',21,'H'],['BAL',2,'A'],['DAL',8,'A'],['ATL',1,'H']]
TEN = [['MIA',18,'A'],['HOU',12,'H'],['JAX',14,'A'],['PHI',25,'H'],['BUF',3,'A'],['BAL',2,'H'],['LAC',16,'A'],['B','Y','E','W','E','E','K'],['DAL',8,'A'],['NE',20,'H'],['IND',13,'A'],['HOU',12,'A'],['NYJ',23,'H'],['JAX',14,'H'],['NYG',22,'A'],['WAS',31,'H'],['IND',13,'H']]
WAS = [['ARI',0,'A'],['IND',13,'H'],['GB',11,'H'],['B','Y','E','W','E','E','K'],['NO',21,'A'],['CAR',4,'H'],['DAL',8,'H'],['NYG',22,'A'],['ATL',1,'H'],['TB',29,'A'],['HOU',12,'H'],['DAL',8,'A'],['PHI',25,'A'],['NYG',22,'H'],['JAX',14,'A'],['TEN',30,'A'],['PHI',25,'H']]

team_schedule = [ARI,ATL,BAL,BUF,CAR,CHI,CIN,CLE,DAL,DEN,DET,GB,HOU,IND,JAX,KC,LAC,LAR,MIA,MIN,NE,NO,NYG,NYJ,OAK,PHI,PIT,SEA,SF,TB,TEN,WAS]

CARDINALS = ['LAR','SEA','SF']
FALCONS = ['CAR','NO','TB']
RAVENS = ['CIN','CLE','PIT']
BILLS = ['MIA','NE','NYJ']
PANTHERS = ['ATL','NO','TB']
BEARS = ['DET','GB','MIN']
BENGALS = ['BAL','CLE','PIT']
BROWNS = ['BAL','CIN','PIT']
COWBOYS = ['NYG','PHI','WAS']
BRONCOS = ['KC','LAC','OAK']
LIONS = ['CHI','GB','MIN']
PACKERS = ['CHI','DET','MIN']
TEXANS = ['IND','JAX','TEN']
COLTS = ['HOU','JAX','TEN']
JAGUARS = ['HOU','IND','TEN']
CHIEFS = ['DEN','LAC','OAK']
CHARGERS = ['DEN','KC','OAK']
RAMS = ['ARI','SEA','SF']
DOLPHINS = ['BUF','NE','NYJ']
VIKINGS = ['CHI','DET','GB']
PATRIOTS = ['BUF','MIA','NYJ']
SAINTS = ['ATL','CAR','TB']
GIANTS = ['DAL','PHI','WAS']
JETS = ['BUF','NE','MIA']
RAIDERS = ['DEN','KC','LAC']
EAGLES = ['DAL','NYG','WAS']
STEELERS = ['BAL','CIN','CLE']
SEAHAWKS = ['ARI','LAR','SF']
N49ERS = ['ARI','LAR','SEA']
BUCCANEERS = ['ATL','CAR','NO']
TITANS = ['HOU','IND','JAX']
REDSKINS = ['DAL','NYG','PHI']

league_standing = []

division_scores = [CARDINALS,FALCONS,RAVENS,BILLS,
                   PANTHERS,BEARS,BENGALS,BROWNS,
                   COWBOYS,BRONCOS,LIONS,PACKERS,
                   TEXANS,COLTS,JAGUARS,CHIEFS,
                   CHARGERS,RAMS,DOLPHINS,VIKINGS,
                   PATRIOTS,SAINTS,GIANTS,JETS,
                   RAIDERS,EAGLES,STEELERS,SEAHAWKS,
                   N49ERS,BUCCANEERS,TITANS,REDSKINS]

division_stat = []

current_team = ['CARDINALS ',
                'FALCONS   ',
                'RAVENS    ',
                'BILLS     ',
                'PANTHERS  ',
                'BEARS     ',
                'BENGALS   ',
                'BROWNS    ',
                'COWBOYS   ',
                'BRONCOS   ',
                'LIONS     ',
                'PACKERS   ',
                'TEXANS    ',
                'COLTS     ',
                'JAGUARS   ',
                'CHIEFS    ',
                'CHARGERS  ',
                'RAMS      ',
                'DOLPHINS  ',
                'VIKINGS   ',
                'PATRIOTS  ',
                'SAINTS    ',
                'GIANTS    ',
                'JETS      ',
                'RAIDERS   ',
                'EAGLES    ',
                'STEELERS  ',
                'SEAHAWKS  ',
                '49ERS     ',
                'BUCCANEERS',
                'TITANS    ',
                'REDSKINS  ']

#print(team_schedule[31][16])

for GAME in range(17):

    for TEAM in range(32):

        if (len(team_schedule[TEAM][GAME]) == 3):

            #print("WEEK",GAME+1, current_team[TEAM], 'vs.', current_team[team_schedule[TEAM][GAME][1]])

            if (team_schedule[TEAM][GAME][2] == 'H'):

                print('------------------------------------------')
                print('                  WEEK', GAME + 1)
                print('------------------------------------------')
                print('\t\t', current_team[TEAM], ' vs. ', current_team[team_schedule[TEAM][GAME][1]])
                print('               @', current_team[TEAM], '')
                print('------------------------------------------')

            else:
                print('------------------------------------------')
                print('                  WEEK', GAME + 1)
                print('------------------------------------------')
                print('\t\t', current_team[TEAM], ' vs. ', current_team[team_schedule[TEAM][GAME][1]])
                print('               @', current_team[team_schedule[TEAM][GAME][1]], '')
                print('------------------------------------------')

            print('          <<< WHO WILL WIN? >>>')
            print('------------------------------------------')
            print('1 =', current_team[TEAM])
            print('2 =', current_team[team_schedule[TEAM][GAME][1]])
            print('------------------------------------------')

            win_loss = input()
            #win_loss = random.randint(1, 2)
            print(win_loss)

            print('------------------------------------------')
            print()


            if (win_loss == '1'):
                team_schedule[TEAM][GAME].append(1)
                team_schedule[team_schedule[TEAM][GAME][1]][GAME].append(0)

            else:
                team_schedule[TEAM][GAME].append(0)
                team_schedule[team_schedule[TEAM][GAME][1]][GAME].append(1)

for TEAM in range(32):

    summ = 0

    for GAME in range(17):

        if(len(team_schedule[TEAM][GAME]) == 4):

            summ += team_schedule[TEAM][GAME][3]

    loss = 16 - summ

    ratioo = summ/16

    ratioo = round(ratioo,3)

    league_standing.append([current_team[TEAM],summ,loss,ratioo])

for TEAM in range(32):

    current_team[TEAM]

    tea = []

    summation = 0

    for i in range(3):

        tea.append(division_scores[TEAM][i])

        for GAME in range(17):

            if(team_schedule[TEAM][GAME][0] == division_scores[TEAM][i]):

                tea.append(team_schedule[TEAM][GAME][3])

    division_stat.append([current_team[TEAM],tea])


for TEAM in range(32):

    division_total = division_stat[TEAM][1][1]+division_stat[TEAM][1][2]+division_stat[TEAM][1][4]+division_stat[TEAM][1][5]+division_stat[TEAM][1][7]+division_stat[TEAM][1][8]

    prcnt = division_total/6

    prcnt = round(prcnt,3)

    if (prcnt == 0.75):

        prcnt = 0.750

    if (prcnt == 0.5):

        prcnt = 0.500

    if (prcnt == 0.25):

        prcnt = 0.250

    division_stat[TEAM].append(prcnt)

    division_stat[TEAM].append(league_standing[TEAM][3])

    division_stat[TEAM].append(division_stat[TEAM][2] + division_stat[TEAM][3])

    division_stat[TEAM].append(league_standing[TEAM][1])

    division_stat[TEAM].append(league_standing[TEAM][2])

NFC = [league_standing[5],
       league_standing[10],
       league_standing[11],
       league_standing[19],
       league_standing[8],
       league_standing[22],
       league_standing[25],
       league_standing[31],
       league_standing[1],
       league_standing[4],
       league_standing[21],
       league_standing[29],
       league_standing[0],
       league_standing[17],
       league_standing[27],
       league_standing[28]]

AFC = [league_standing[2],
       league_standing[6],
       league_standing[7],
       league_standing[26],
       league_standing[3],
       league_standing[18],
       league_standing[20],
       league_standing[23],
       league_standing[12],
       league_standing[13],
       league_standing[14],
       league_standing[30],
       league_standing[9],
       league_standing[15],
       league_standing[16],
       league_standing[24]]

NFC_NORTH = [division_stat[5],division_stat[10],division_stat[11],division_stat[19]]
NFC_EAST = [division_stat[8],division_stat[22],division_stat[25],division_stat[31]]
NFC_SOUTH = [division_stat[1],division_stat[4],division_stat[21],division_stat[29]]
NFC_WEST = [division_stat[0],division_stat[17],division_stat[27],division_stat[28]]

AFC_NORTH = [division_stat[2],division_stat[6],division_stat[7],division_stat[26]]
AFC_EAST = [division_stat[3],division_stat[18],division_stat[20],division_stat[23]]
AFC_SOUTH = [division_stat[12],division_stat[13],division_stat[14],division_stat[30]]
AFC_WEST = [division_stat[9],division_stat[15],division_stat[16],division_stat[24]]

NNsort = []

for i in range(4):
    NNsort.append([NFC_NORTH[i][0],NFC_NORTH[i][2],NFC_NORTH[i][3],NFC_NORTH[i][4],NFC_NORTH[i][5],NFC_NORTH[i][6]])
NEsort = []

for i in range(4):
    NEsort.append([NFC_EAST[i][0],NFC_EAST[i][2],NFC_EAST[i][3],NFC_EAST[i][4],NFC_EAST[i][5],NFC_EAST[i][6]])
NSsort = []

for i in range(4):
    NSsort.append([NFC_SOUTH[i][0],NFC_SOUTH[i][2],NFC_SOUTH[i][3],NFC_SOUTH[i][4],NFC_SOUTH[i][5],NFC_SOUTH[i][6]])
NWsort = []

for i in range(4):
    NWsort.append([NFC_WEST[i][0],NFC_WEST[i][2],NFC_WEST[i][3],NFC_WEST[i][4],NFC_WEST[i][5],NFC_WEST[i][6]])
ANsort = []

for i in range(4):
    ANsort.append([AFC_NORTH[i][0],AFC_NORTH[i][2],AFC_NORTH[i][3],AFC_NORTH[i][4],AFC_NORTH[i][5],AFC_NORTH[i][6]])
AEsort = []

for i in range(4):
    AEsort.append([AFC_EAST[i][0],AFC_EAST[i][2],AFC_EAST[i][3],AFC_EAST[i][4],AFC_EAST[i][5],AFC_EAST[i][6]])
ASsort = []

for i in range(4):
    ASsort.append([AFC_SOUTH[i][0],AFC_SOUTH[i][2],AFC_SOUTH[i][3],AFC_SOUTH[i][4],AFC_SOUTH[i][5],AFC_SOUTH[i][6]])
AWsort = []

for i in range(4):
    AWsort.append([AFC_WEST[i][0],AFC_WEST[i][2],AFC_WEST[i][3],AFC_WEST[i][4],AFC_WEST[i][5],AFC_WEST[i][6]])


NNsort = sorted(NNsort, key = itemgetter(2))
NEsort = sorted(NEsort, key = itemgetter(2))
NSsort = sorted(NSsort, key = itemgetter(2))
NWsort = sorted(NWsort, key = itemgetter(2))

ANsort = sorted(ANsort, key = itemgetter(2))
AEsort = sorted(AEsort, key = itemgetter(2))
ASsort = sorted(ASsort, key = itemgetter(2))
AWsort = sorted(AWsort, key = itemgetter(2))

di_titles = ['AFC NORTH','AFC EAST','AFC SOUTH','AFC WEST','NFC NORTH','NFC EAST','NFC SOUTH','NFC WEST']
Final_division_standings = [ANsort,AEsort,ASsort,AWsort,NNsort,NEsort,NSsort,NWsort]
print()

for i in range(8):
    print('__________________')
    print('    ',di_titles[i])
    print('__________________')
    print(Final_division_standings[i][3][0]," {}-{}".format((Final_division_standings[i][3][4]), Final_division_standings[i][3][5]))
    print(Final_division_standings[i][2][0]," {}-{}".format((Final_division_standings[i][2][4]), Final_division_standings[i][2][5]))
    print(Final_division_standings[i][1][0]," {}-{}".format((Final_division_standings[i][1][4]), Final_division_standings[i][1][5]))
    print(Final_division_standings[i][0][0]," {}-{}".format((Final_division_standings[i][0][4]), Final_division_standings[i][0][5]))
    print()

print()


print("_____________________________")
print()
print("      LEAGUE STANDINGS")

league_standing = sorted(league_standing, key = itemgetter(3))

AFC = sorted(AFC, key = itemgetter(3))

NFC = sorted(NFC, key = itemgetter(3))

league_standing = sorted(league_standing, key = itemgetter(3))
print("_____________________________")
print("            AFC   ")
print("_____________________________")
for i in range(16):

        print(AFC[-i-1])

print()
print("_____________________________")
print("            NFC   ")
print("_____________________________")
for i in range(16):

        print(NFC[-i-1])

    #print(league_standing[-i-1])

print()
print()
print("_____________________________________________________________")
print()
print("DIVISIONAL STATISTICS AND DATA")
print()
print("_____________________________________________________________")
print("TEAM NAME                  DIVISION W/L                W/L %")
print("_____________________________________________________________")
for GAME in range(32):
    print(division_stat[GAME][:3])

print()
print()
print()
print("________________________________________________")
print()
print("2018 LEAGUE SCHEDULE COMPLETED")
print("________________________________________________")



for GAME in range(17):

    print("________________________________________________")
    print("WEEK ", GAME + 1, " TOTAL                WINNER" )
    print("________________________________________________")

    for TEAM in range(32):

        if (len(team_schedule[TEAM][GAME]) == 4):

            if ((team_schedule[TEAM][GAME][3]) == 1):

                print(current_team[TEAM],' vs ',current_team[team_schedule[TEAM][GAME][1]],' | ',current_team[TEAM])
    print()








