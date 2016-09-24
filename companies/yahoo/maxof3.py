import sys

def maxof3(l):
	max1 = -sys.maxint-1
	max2 = None
	max3 = None
	min1 = sys.maxint
	min2 = None
	for n in l:
		if max1<n:
			max3=max2
			max2=max1
			max1=n
		elif max2<n:
			max3=max2
			max2=n
		elif max3<n:
			max3=n

		if min1>n:
			min2=min1
			min1=n
		elif min2>n:
			min2=n
			
	p1 = (max1*max2*max3, (max1, max2, max3))
	p2 = (max1*min1*min2, (max1, min1, min2))
	return max(p1,p2)

def main():
	l = [10, 1, 2, 3, 6, -5, -10]
	print maxof3(l)

if __name__=="__main__":
	main()