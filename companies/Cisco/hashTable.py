HTSize = 16

class HashEntry(object):
	def __init__(self, mac=None, port=None, hashIndex=None):
		self.entry = (mac, port, hashIndex)
		self.nextEntry = None

	def getEntry(self):
		return self.entry

	def clearEntry(self):
		self.entry = (None, None, None)

class HashTable(object):
	def __init__(self):
		self.table = []
		self.sTop = None    #used Top

		ptr  = HashEntry()  #temp pointer
		self.uTop = ptr     #unused Top

		self.table.append(ptr)
		for i in range(1,HTSize): #notice HTSize is as defined above
			ptr2 = HashEntry()
			ptr.nextEntry = ptr2
			self.table.append(ptr)
			ptr = ptr2

	def printHashTable(self):
		ptr = self.uTop
		for e in self.table:
			print e.entry

	def getEntry(self, mac):
		hashIndex = calcHash(mac)
		return self.table[hashIndex]

	def putEntry(self, mac, port):
		hashIndex = calcHash(mac)
		if not self.table[hashIndex].mac:
			self.table[hashIndex] = HashEntry(mac, port)
		else:
			#handle collision
			emptySlot = self.uTop
			self.uTop = self.uTop.nextEntry
			emptySlot = HashEntry(mac,port)

			ptr = self.table[hashIndex]
			while ptr.hashIndex:
				newIndex = ptr.hashIndex
				ptr = self.table[newIndex]
			ptr.hashIndex = self.table.index(emptySlot) #index of empty slot

			#update uTop
			#find next emptySlot in the list after emptySlot

	def calcHash(self, mac):
		macList = mac.split(':')
		hashIndex = int(macList[-1],16)%HTSize
		return hashIndex

def main():

if __name__ == "__main__":
	main()