#Without using additional data structure u can do this in O(nlogn)
#by sorting both the lists

from collections import Counter

def intersect(l1, l2):
	c = Counter(l1)
	res = []

	for n in l2:
		if n in c:
			res.append(n)
			c[n]-=1
	return res

def intersectCnt(l1, l2):
	c1 = Counter(l1)
	c2 = Counter(l2)
	c = c1 & c2
	res = []
	for k,v in c.items():
		res.extend([k]*c[k])
	return res

def main():
	l1 = [1, 2, 2, 3, 4, 5, 5, 2]
	l2 = [1, 2, 3, 2, 6, 7]
	print intersect(l1, l2)

if __name__ == "__main__":
	main()