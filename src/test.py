from random import randint

print("Debut du programme")

# Variables de configuration

total_simulations = 100000
nb_simulations = total_simulations
seuil = 26



curr_simulation = 0

max_uniques = 1
somme_uniques = 0
min_uniques = 37
gain_min = 0
gain_max = 0
sum_gain = 0
min_l = 10000
max_l = 0
min_w = 10000
max_w = 0
sum_w = 0
sum_l = 0

max_bet = 1

print(nb_simulations)

stats = {0: [0, 0, 0]}

for i in range(1,37):
	stats[i] = [0, 0, 0]

print(stats)

game = 1

while game <= total_simulations:
	print("Debut du jeu {0}".format(game))
	game += 1
	nb_spins = 37
	results = []
	tot_gain = 0
	l = 0
	w = 0
	bet = 1
	while nb_spins > 0:
		print("Spin = {0}".format(37 - nb_spins + 1))
		prevSet = set(results)
		if len(prevSet) < seuil :
			print("{0} => on ne joue pas".format(len(prevSet)))
			if nb_spins < 8 :
				print("FIN DU JEU gain 0")
				break
		else :
			print("{0} => on joue !".format(len(prevSet)))
			if tot_gain > 0:
				print("FIN DU JEU gain {0}".format(tot_gain))
				break

			# on determine le bet pour couvrir la perte
			if tot_gain < 0:
				print("perte en cours : {0}".format(tot_gain))
				bet = -1 * tot_gain / (35 - len(prevSet)) + 1
			print("bet => {0}".format(bet))
			if bet > max_bet:
				max_bet = bet

		result = randint(0, 36)
		results.append(result)
		newSet = set(results)
		stats[len(prevSet)][0] += 1
		if len(newSet) > len(prevSet):
			print("new")
			stats[len(prevSet)][1] += 1
			if (len(prevSet) >= seuil):
				gain = bet * len(prevSet)
				print("perdu {0}".format(gain))
				tot_gain -= gain
				bet += 1
				l += 1
		else:
			print("old")
			stats[len(prevSet)][2] += 1
			if (len(prevSet) >= seuil):
				gain = bet * (35 - len(prevSet))
				print("gagne {0}".format(gain))
				tot_gain += gain
				if bet > 1:
					bet -= 1
				w += 1
		nb_spins -= 1

		# print("tirage {0}".format(37 - nb_spins + 1))
		# print("result : {0}".format(result))

	s = set(results)
	# print("final result : {0}".format(s))
	# print("Nombre de chiffres uniques {0}".format(len(s)))
	curr_simulation += 1
	# print("Rotation {0}".format(curr_simulation))
	if max_uniques < len(s):
		max_uniques = len(s)
	if min_uniques > len(s):
		min_uniques = len(s)
	somme_uniques += len(s)
	nb_simulations -= 1
	if tot_gain > gain_max:
		gain_max = tot_gain
	if tot_gain < gain_min:
		gain_min = tot_gain
	sum_gain += tot_gain
	if w < min_w:
		min_w = w
	if w > max_w:
		max_w = w
	if l < min_l:
		min_l = l
	if l > max_l:
		max_l = l
	sum_l += l
	sum_w += w


print("Maximun uniques {0}".format(max_uniques))
moy = float(somme_uniques) / float(curr_simulation)
print("Moyenne uniques {0}".format(moy))
print("Minumum uniques {0}".format(min_uniques))

print("#### Gains")
print(sum_gain)
moy_gain = float(sum_gain) / float(total_simulations)
print(moy_gain)
print(gain_min)
print(gain_max)

print("####")

print("max bet {0}".format(max_bet))

print("#### Coups")

moy_l = float(sum_l) / float(total_simulations)
moy_w = float(sum_w) / float(total_simulations)
print(min_l)
print(max_l)
print(moy_l)
print(min_w)
print(max_w)
print(moy_w)

print("####")

print(stats)

# for i in range(1, 37):
# 	if stats[i][0] > 0:
# 		print("##### niveau {0}".format(i))
# 		ancien = stats[i][2] / stats[i][0]
# 		nouveau = stats[i][1] / stats[i][0]
# 		# print float(stats[i][2]) / float(stats[i][0])
# 		# print float(stats[i][1]) / float(stats[i][0])		
# 		print("=> si mise sur ancien")
# 		gain = 35 - i
# 		perte = i
# 		# print("gain potentiel {0}".format(gain))
# 		# print("perte potentielle {0}".format(perte))
# 		espG = float(gain) * float(stats[i][2]) / float(stats[i][0])
# 		espP = float(perte) * float(stats[i][1]) / float(stats[i][0])
# 		esp = espG - espP
# 		# print espG
# 		# print float(espG)
# 		# print espP
# 		# print float(espP)
# 		print esp
# 		print("=> si mise sur nouveau")
# 		gain = 35 - (37 - i)
# 		perte = (37 - i)
# 		espG = float(gain) * float(stats[i][1]) / float(stats[i][0])
# 		espP = float(perte) * float(stats[i][2]) / float(stats[i][0])
# 		esp = espG - espP
# 		print esp