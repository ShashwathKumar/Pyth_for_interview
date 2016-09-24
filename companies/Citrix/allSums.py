#represent a given number in all possible sums

def partition(n):
	partition_rec(n, n, '')

def partition_rec(n, maxy, prefix):
	if n==0:
		print prefix
		return

	i = min(n, maxy)
	while i>=1:
		print '-',
		partition_rec(n-i, i, prefix+' '+str(i))
		i-=1

def main():
	partition(5)

if __name__=="__main__":
	main()