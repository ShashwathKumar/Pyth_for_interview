def translate():
	n = int(raw_input())
	langD = {}
	wtD   = {}
	for i in xrange(n):
		s = raw_input()
		sl = s.split()
		langD[sl[0]] = sl[2]
		wtD[sl[2]]   = sl[1]
	sent = raw_input()
	sentL = sent.split()
	l = []
	#print langD
	#print wtD
	for word in sentL[1:]:
		if word in langD:
			wt = langD[word]
			l.append((wtD[wt], wt))
	l = sorted(l, key=lambda x: x[1], reverse=True)
	#print l
	newSent = map(lambda x: x[0], l)
	print ' '.join(newSent)


translate()