import random
import matplotlib.pyplot as plt

dataRange = 100
W = [0.5,0.5]
bias = 0.5
alpha = 1
X = []
t = []

for i in range(dataRange):
	a = random.random()
	b = random.random()
	X.append([a,b])
	if(a+b-1>0):
		t.append(1)
	else:
		t.append(-1)

print(X,t)

def sortieCalc(num):
	y = bias+X[num][0]*W[0]+X[num][1]*W[1]
	if(y>=0):
		return 1
	else:
		return -1

def correctWeight(num):
	e = t[num]-sortieCalc(num)
	if(e!=0):
		global bias
		global W
		bias+= e*alpha
		W = [W[0]+e*X[num][0],W[1]+e*X[num][1]]
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
	sortie.append(sortieCalc(i)-t[i])

print(sortie,W,bias)
plt.plot(nums,errors)
plt.show()
