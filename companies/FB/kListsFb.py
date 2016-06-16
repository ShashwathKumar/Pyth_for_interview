import sys

l=[]
a = [1, 4, 6, 7, 34]
b = [2 , 3, 4, 34, 67]
c = [2, 3, 5, 67, 97]
l.append(a)
l.append(b)
l.append(c)
k = 3

def findMin():
	min = sys.maxint
	for i in range(k):
		if l[i][0] < min:
			min = l[i][0]
	return min

def minTerator():
    minNum = findMin()

    for j in range(k):
    	if minNum == l[j][0]:
    		l[j].pop(0)
    		break

    return minNum
    
for i in range(10):
	print minTerator()
	print l
