from random import randint

# Tools
def log(msg, lvl):
    if lvl <= LOG_LEVEL:
    	print msg
    	return



# Variables de configuration

MAX_SIMULATIONS = 5000
SEUIL_START = 18
NB_SPINS = 37

# O => aucun log, 1 => que des logs importants, 2 => tous les logs
LOG_LEVEL = 2



print("Start")

log("niveau de logs : {0}".format(LOG_LEVEL), 1)

game = 1

total_wins = 0
total_lose = 0
max_wins = 0
max_lose = 100

stats = {0: [0, 0, 0]}

for i in range(1,4000):
	stats[i] = [0, 0, 0]

while game <= MAX_SIMULATIONS:
	log("Debut du jeu {0}".format(game), 2)

	results = []

	l = 0
	w = 0

	spin = 1

	while spin <= NB_SPINS:

		log("Spin = {0}".format(spin), 2)
		prevSet = set(results)
		stats[len(prevSet)*100+spin][0] += 1
		play = 0
		log(len(prevSet), 2)
		# On ne joue qu'a partir d'un seuil
		if len(prevSet) > SEUIL_START:
			play = 1
		result = randint(0, 36)
		results.append(result)
		newSet = set(results)
		if play > 0:
			if len(newSet) > len(prevSet):
				log("lose", 2)
				stats[len(prevSet)*100+spin][2] += 1
				l += 1
			else:
				log("win", 2)
				stats[len(prevSet)*100+spin][1] += 1
				w += 1
		spin += 1

	total_wins += w
	total_lose += l
	log(w, 2)
	log(l, 2)



	game += 1
	log(game, 1)


# for i in range(1, 37):
# 	for j in range(1, 37):
# 		index = i*100+j
# 		if stats[index][0]>0:
# 			log("niveau {0}; coup {1}".format(i, j), 1)
# 			log(stats[index],1)
