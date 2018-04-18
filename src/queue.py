from random import randint
from collections import deque

# Tools
def log(msg, lvl):
    if lvl <= LOG_LEVEL:
        print msg
        return



# Variables de configuration

MAX_SIMULATIONS = 100000

MAX_LEN = 37

START_BET = 27

# O => aucun log, 1 => que des logs importants, 2 => tous les logs
LOG_LEVEL = 2

print("Start")

log("niveau de logs : {0}".format(LOG_LEVEL), 1)

spin = 1
q = deque()

gain = 0
bet = 0

max_bet = 0
max_mise = 0
min_gain = 0
max_gain = 0

# Stats base sur le prev set
# stats = { 13: [0, 0, 0, 0] }
# Base sur le new Set
stats2 = { 13: [0, 0, 0, 0] }
for i in range(13, 35):
	# stats[i] = [0, 0, 0, 0]
	stats2[i] = [0, 0, 0, 0]

while spin <= MAX_SIMULATIONS:
    result = randint(0, 36)
    if len(q) == MAX_LEN:
    	# prevLen = len(set(q))
    	# stats[prevLen][0]+= 1
        q.pop()
        currLen = len(set(q))
        stats2[currLen][0] += 1

        bet = max(0, (currLen - START_BET)*5)
        if bet > max_bet:
        	max_bet = bet

        mise = bet * currLen

        q.appendleft(result)
        # print q
        newLen = len(set(q))

        
        print("lvl {0} => bet {1}".format(currLen, bet))
        print("lvl {0} => mise {1}".format(currLen, mise))

        if mise > max_mise:
        	max_mise = mise

        # # 1 prev 
        # if prevLen > newLen:
        # 	stats[prevLen][1]+=1
        # if prevLen == newLen:
        # 	stats[prevLen][2]+=1
        # if prevLen < newLen:
        # 	stats[prevLen][3]+=1

        #2 curr
        if currLen > newLen:
        	# ne peut pas arriver
        	stats2[currLen][1]+=1
        if currLen == newLen:
        	if bet > 0:
        		gain += 35 * bet - mise
        		print "gagne {0}".format(35*bet-mise)
        	stats2[currLen][2]+=1
        if currLen < newLen:
        	if bet > 0:
        		gain -= mise
        		print "perdu {0}".format(mise)
        	stats2[currLen][3]+=1
    else:
    	q.appendleft(result)
    	# print q
    spin+=1
    print gain
    if gain > max_gain:
    	max_gain = gain
    if gain < min_gain:
    	min_gain = gain

print "Fin du jeu"

print "Bet max {0}".format(max_bet)
print "Mise max {0}".format(max_mise)
print "Gain mini {0}".format(min_gain)
print "Gain maxi {0}".format(max_gain)

# for i in range(13, 35):
# 	print("{0}\t{1}\t{2}\t{3}\t{4}".format(i, stats[i][0], stats[i][1], stats[i][2], stats[i][3]))

# for i in range(13, 35):
# 	print("{0}\t{1}\t{2}\t{3}\t{4}".format(i, stats2[i][0], stats2[i][1], stats2[i][2], stats2[i][3]))