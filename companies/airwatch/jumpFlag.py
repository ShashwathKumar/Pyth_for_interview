def jumps(k, j):
	cnt = 0
	while k>=j:
		k-=j
		cnt+=1
	cnt+=k
	return cnt