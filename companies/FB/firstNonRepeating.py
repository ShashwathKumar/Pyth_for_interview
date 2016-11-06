#Given an array of positive integers, print the first non-repeating integer

def firstNonRepeating(arr):
	tmpD = {}
	tmpS = set()
	for i, n in enumerate(arr):
		if n not in tmpS:
			if n in tmpD:
				del tmpD[n]
				tmpS.add(n)
			else:
				tmpD[n]=i
	firstUnique = None
	firstIndex  = len(arr)
	for k,v in tmpD.items():
		if v<firstIndex:
			firstUnique = k
			firstIndex  = v
	return firstUnique

def main():
	arr = [1, 1, 7, 2, 7, 3, 4, 3, 5, 4]
	print firstNonRepeating(arr)

if __name__=="__main__":
	main()