import random
import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

Liste = []
Res = []

for i in range(30):
	Coord = [[random.random(),random.random()]]

	if (0.3<Coord[0][0]<0.7 and 0.3<Coord[0][1]<0.7):
		res = 1
	else:
		res = 0

	Coord.append(res)
	Liste.append(Coord)


