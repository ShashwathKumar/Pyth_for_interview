import sys
class node(Object):
	def __init__(self):
		self.val = -1
		self._next = None

class myLL(Object):
	def __init__(self, head):
		self.h = head
		self.length = self.findLen()
		self.diff = []
		self.lastLength = []

	def findLen(self):
		cnt=0
		node=self.h
		while node:
			cnt+=1
			node=node._next
		return cnt

def threeLL(heads):
	lls = []
	for head in heads:
		lls.append(myLL(head))
	llLength = len(lls)
	for ll in lls:
		ll.lastLength = [-1 for i in xrange(llLength)]

	#Difference of length of each LL with other
	for ll in lls:
		for tmpLL in lls:
			ll.diff.append(ll.length-tmpLL.length)

	for i,ll in enumerate(lls):
		j=i+1
		while j<llLength:
			lastLength = findLastLength(lls, i, j)
			lls[i].lastLength[j] = lls[j].lastLength[i] = lastLength

	minLastLength = (sys.maxint,sys.maxint)
	for i,ll in enumerate(lls):
		tmpL = [n for n in ll[i].lastLength if n!=-1]
		if len(tmpL)==0 and len(tmpL) < minLastLength[0]:
			minLastLength = (tmpL, i)





