from collections import deque

class Lru(object):
	class LinkedListNode(object):
		def __init__(self, k,v):
			self.key   = k
			self.value = v

	def __init__(self, maxSize):
		self.maxSize = maxSize
		self.dll     = deque()
		self.kdict   = {}

	def setPair(self, k, v):
		node = None
		if k in self.kdict:
			node = self.kdict[k]
			self.removeKey(k, node)
		else:
			node = self.LinkedListNode(k,v)
			if self.full():
				self.removeLru()
				#print "#################", self.kdict
		self.putDict(k, node)
		self.insertTop(node)

	def getVal(self, k):
		if k in self.kdict:
			node = self.kdict[k]
			self.removeFromDll(node)
			self.insertTop(node)
			return node.value

	def removeKey(self, k, node): #removes from DLL also
		del self.kdict[k]
		self.removeFromDll(node)

	def removeFromDll(self, node):
		self.dll.remove(node)

	def insertTop(self, node):
		self.dll.appendleft(node)

	def putDict(self, k, node):
		self.kdict[k] = node

	def removeLru(self):
		node = self.dll.pop()
		key = [k for k,v in self.kdict.items() if v==node][0]
		del self.kdict[key]

	def full(self):
		return len(self.kdict)==self.maxSize


def main():
	c = Lru(5)
	c.setPair('a', 'apple')
	c.setPair('b', 'bat')
	c.setPair('c', 'cat')
	c.setPair('d', 'dynamite')
	print c.dll
	print c.kdict
	print
	print "-------------------------------------------------------------"
	print c.getVal('a')
	print c.dll
	print c.kdict
	print	
	print "-------------------------------------------------------------"
	c.setPair('e', 'effulgence')
	c.setPair('f', 'factory')
	print c.dll
	print c.kdict
	print	
	print "-------------------------------------------------------------"

if __name__ == "__main__":
	main()