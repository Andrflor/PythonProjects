W = [-0.7,0.2]
bias = 0.5
alpha = 1
X = [[2,1],[0,-1],[-2,1],[0,2]]
t = [1,1,-1,-1]
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

while not finish:
	errors = []
	for i in range(len(X)):
		errors.append(correctWeight(i))
	if(errors[0]==0 and errors[1]==0 and errors[2]==0 and errors[3]==0):
		finish = True
		print([sortieCalc(0),sortieCalc(1),sortieCalc(2),sortieCalc(3)],W,bias)
