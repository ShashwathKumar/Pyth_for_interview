#orderedDict
#Counter -- odd even
from collections import Counter

def funpal(s):
	c = Counter(s)
	odds=[]
	evens=[]
	cl = c.most_common()
	cl = map(list,cl)
	for t in cl:
		evens.append(t) if t[1]%2==0 else odds.append(t)
	evens2=[]
	for t in evens:
		if t[1]>2:
			t[1]/=2
			print t
			evens2.append(t) #need to append copy(t)
	a = formpal(odds.pop(0), evens)
	b = formpal(odds.pop(0), evens2)
	return a,b, len(a)*len(b)

def formpal(oddTuple, evens):
	print evens
	xl = []
	xl.append(oddTuple[0]*(oddTuple[1]/2))
	#evens
	for t in evens:
		t[1]/=2
		xl.append(t[0]*t[1])
	xl.append(oddTuple[0])
	#evens in reverse
	for t in reversed(evens):
		xl.append(t[0]*t[1])
	xl.append(oddTuple[0]*(oddTuple[1]/2))
	return ''.join(xl)

def main():
	s = 'aabbbccxxffrrrrt'
	print funpal(s)

if __name__ == "__main__":
	main()