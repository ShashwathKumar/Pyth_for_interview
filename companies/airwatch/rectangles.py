from collections import Counter

def rectangles():
	n = int(raw_input())
	for i in xrange(n):
		dummy  = raw_input()
		sticks = raw_input()
		stickL = sticks.split()
		stickCount = Counter(stickL)
		for k in stickCount:
			v = stickCount[k]
			stickCount[k] = v/2
		totalPairs = sum(stickCount.values())
		print totalPairs/2

rectangles()