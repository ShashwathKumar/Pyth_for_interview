def sqs(n):
	if n<=3:
		return n
	res = n #initializing n to max possible value

	for i in xrange(4, n+1):
		tmp = i**2
		if tmp>n:
			break
		else:
			res = min(res, 1+sqs(n-tmp))
	return res

def sqsDp(n):
	sqs = [0 for n in xrange(n+1)] #its imp that sqs[0]=0
	sqs[1]=1
	sqs[2]=2
	sqs[3]=3

	for i in xrange(4, n+1):
		sqs[i]=i

		for j in xrange(1, int(i**0.5+1)):
			tmp = j**2
			sqs[i] = min(sqs[i], 1+sqs[i-tmp])
	print sqs
	return sqs[n]

def main():
	print sqsDp(18)
	
if __name__=="__main__":
	main()