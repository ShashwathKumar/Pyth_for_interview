def lcs(a,b):
	#In this logic, among the subsequences the one which appears in a first
	#will appear in the result
	lena = len(a)
	lenb = len(b)
	c = [[0 for bx in xrange(lenb)] for ax in xrange(lena)]

	for i in xrange(lena):
		for j in xrange(lenb):
			if a[i]==b[j]:
				prev    = c[i-1][j-1] if i>0 and j>0 else 0
				c[i][j] = prev+1
			else:
				prevUp    = c[i-1][j] if i>0 else 0 
				prevLeft  = c[i][j-1] if j>0 else 0
				c[i][j]   = max(prevUp, prevLeft)
	
	sub = []
	prev=i=j=0
	while i < lena:
		j=-1
		while j < lenb-1:
			if c[i][j+1]>prev:
				sub.append(b[j+1])
				prev=c[i][j+1]
			elif i<lena-1 and j<lenb-1 and c[i+1][j+1]>prev:
				sub.append(b[j+1])
				prev=c[i+1][j+1]
				i+=1
			j+=1
		i+=1
	printMat(c)
	return c[lena-1][lenb-1], ''.join(sub)

def printMat(c):
	for r in c:
		for ch in r:
			print ch,
		print

def main():
	a = 'abcccda'
	b = 'accada'
	print lcs(a,b)

if __name__=="__main__":
	main()