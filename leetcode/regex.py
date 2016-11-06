def regex(p1, p2): #assuming p2 is the regex pattern
	length1 = len(p1)+1
	length2 = len(p2)+1
	m = [[False for j in xrange(length2)] for i in xrange(length1)]
	m[0][0]=True

	i=1
	j=1
	while i<length1:
		while j<length2:
			if p1[i-1]==p2[j-1] or p2[j-1]=='.':
				m[i][j]=m[i-1][j-1]
			elif p2[j-1]=='*': #if this is a valid pattern '*' has to appear at a j>=2
					m[i][j]==m[i][j-2] or ((p1[i-1]==p2[j-2] or p2[j-2]=='.') and m[i-1][j])
			j+=1
		i+=1

	for ar in m:
		print ar

	return m[length1-1][length2-1]

def main():
	p1 = 'xaaacde'
	p2 = 'xa*b*c.e'
	print regex(p1, p2)

if __name__=="__main__":
	main()