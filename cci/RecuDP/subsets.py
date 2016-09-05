from copy import deepcopy

def subsets(s):
	l = list(s)
	sets = [set()]

	for m in l:
		sets.extend(deepcopy(sets))
		x = len(sets)/2
		print x
		for xs in sets[x:]:
			xs.add(m)

	return sets

def subsets2(s):
	length = len(s)
	l = list(s)
	total  = 2**length
	sets = []

	for i in xrange(total):
		tmp = set()
		k=0
		while i:
			if i & 1:
				tmp.add(l[k])
			i>>=1
			k+=1
		sets.append(tmp)

	return sets

def main():
	s = set([1, 2, 3, 4])
	print subsets(s)
	print subsets2(s)

if __name__ == "__main__":
	main()