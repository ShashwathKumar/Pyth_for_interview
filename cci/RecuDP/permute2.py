def permute(s):
	ansL = []

	for c in s:
		if ansL:
			tmpL = []
			for st in ansL:
				tmpL += addCh(st, c)
			ansL = tmpL
		else:
			ansL.append(c)
	return ansL

def addCh(st, c):
	tmpL = []
	i = 0
	n = len(st)

	while i<=n:
		if i == 0:
			tmpL.append(c+st)
		elif i==n:
			tmpL.append(st+c)
		else:
			tmpL.append(st[:i]+c+st[i:])
		i+=1
	return tmpL

def main():
	s = 'abcd'
	print permute(s)

if __name__=="__main__":
	main()