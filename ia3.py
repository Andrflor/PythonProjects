import random
import matplotlib.pyplot as plt

dataRange = 30
W = []
bias = []
alpha = 1
X = []
t = []
layer=3

for i in range(layer):
	W.append([0.5,0.5])
	bias.append(0.5)

print(W,bias)

for i in range(dataRange):
	a = random.uniform(-1,1)
	b = random.uniform(-1,1)
	X.append([a,b])
	if(a<0 and b<0):
		t.append(1)
	else:
		t.append(-1)

print(t)

def sortieCalc(num,lnum):
	y = bias[lnum]+X[num][0]*W[lnum][0]+X[num][1]*W[lnum][1]
	if(y>=0):
		return 1
	else:
		return -1

def outputCalc(values):
	y = bias[layer-1]+values[0]*W[layer-1][0]+values[1]*W[layer-1][1]
	if(y>=0):
		return 1
	else:
		return -1

def correctWeight(num):
	sorties = []
	global bias
	global W
	for l in range(layer-1):
		sorti = sortieCalc(num,l)
		sorties.append(sorti)
		e = t[num]- sorti
		if(e!=0):
			bias[l]+= e*alpha
			W[l] = [W[l][0]+e*X[num][0],W[l][1]+e*X[num][1]]
	e=t[num]-outputCalc(sorties)
	if(e!=0):
		bias[layer-1]+= e*alpha
		W[layer-1] = [W[layer-1][0]+e*sorties[0],W[layer-1][1]+e*sorties[1]]
	return e

finish = False
errors = []
nums = []
num = 0

while not finish:
	error = 0
	finish = True
	for i in range(len(X)):
		if(correctWeight(i)!=0):
			error+=1
			finish = False
	errors.append(error)
	nums.append(num)
	num+=1

sortie = []
for i in range(len(X)):
	sortie.append(sortieCalc(i,layer-1)-t[i])

print(sortie,W,bias)
plt.plot(nums,errors)
plt.show()
