PARTONE = False

with open("2.txt") as file:
	cont = list(map(lambda x: [x[0],x[2]], file.readlines()))

# a, x = rock
# b, y = paper
# c, z = scis

def RunPartOne(cont):
	point = 0
	for game in cont:
		them = ord(game[0])-65
		me  =  ord(game[1])-88

		draw = them==me
		win  = them==(me+2)%3
		lose = not(draw+win)
		result = "draw" if draw else ("win" if win else "lost")

		# +1 since rock=0, but rock's point = 1
		point += (6*win+3*draw)+me+1

		# 23 = diff A->X
		#print(f"{them}X{me} -> {result} = {point}")
	return point

if PARTONE:
	print(RunPartOne(cont))
else:
	# X = lose, Y = draw, Z = win
	for i in range(len(cont)):
		game = cont[i]

		them = ord(game[0])-65
		me  =  ord(game[1])-88

		lose, draw, win = map(lambda x: me==x, (0, 1, 2))
		play = 0
		if draw:
			play = them
		elif win:
			play = (them+4)%3
		else:
			play = (them+2)%3

		cont[i][1] = chr(88+play)
	print(RunPartOne(cont))

