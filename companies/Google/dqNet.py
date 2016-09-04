from collections import deque

def getSet(netL, s,val):
	for sx in netL:
		if val in sx:
			s = sx
			return netL, s #present
	s = set([val])
	netL.append(s)
	return netL, s

def networks(deq, l):
	netL = []
	setl = set(l)
	vmap = {}
	imap = {}

    #populating dmap
	for i, n in enumerate(deq): 
		imap[i] = n
		vmap[n] = i

	for val in l:
		s = None
		netL, s = getSet(netL, s, val)
		#print netL, s

		i = vmap[val]
		if i-1 in imap:
			vPrev=imap[i-1]
			if vPrev in setl:
				s.add(vPrev)
		if i+1 in imap:
			vNext=imap[i+1]
			if vNext in setl:
				s.add(vNext)

	#union the netL
	for i, sx in enumerate(netL):
		j=i+1
		while j<len(netL):
			if sx & netL[j]:
				sx |= netL[j]
				netL.pop(j)
			j+=1

	#print netL
	return len(netL)

def main():
	d = deque([1,2,3,4,5,6,7,8])
	l = [2,5,6,8,1,3, 4]
	print networks(d, l)

if __name__=="__main__":
	main()