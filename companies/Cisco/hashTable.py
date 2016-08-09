HTSize = 16

class HashEntry(object):
	def __init__(self, mac=None, port=None, nextHashIndex=None):
		self.entry = [mac, port, nextHashIndex]
		self.nextEntry = None

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
			self.table.append(ptr2)
			ptr = ptr2

	def printHashTable(self):
		ptr = self.uTop
		for e in self.table:
			print e.entry

	def getEntry(self, mac):
		hashIndex = self.calcHash(mac)
		return self.table[hashIndex]

	def putEntry(self, mac, port):
		hashIndex = self.calcHash(mac)
		if not self.table[hashIndex].entry[0]:  #this refers to mac address
			self.table[hashIndex] = HashEntry(mac, port)
		else:
			#handle collision
			emptySlot = self.uTop
			self.uTop = self.uTop.nextEntry
			emptySlot.entry[0]=mac
			emptySlot.entry[1]=port

			ptr = self.table[hashIndex]
			while ptr.entry[2]: #this refers to nextHashIndex
				newIndex = ptr.entry[2]
				ptr = self.table[newIndex]
			ptr.entry[2] = self.table.index(emptySlot) #index of empty slot

			#update sTop
			

	def calcHash(self, mac):
		macList = mac.split(':')
		hashIndex = int(macList[-1],16)%HTSize
		return hashIndex

def main():
	ht = HashTable()
	ht.printHashTable()
	print "------------------------------------------------"
	ht.putEntry('12:34:4C:31:1A:1B',6)
	ht.printHashTable()
	print "------------------------------------------------"
	ht.putEntry('12:34:4C:31:1A:2B',7)
	ht.putEntry('12:34:4C:31:1A:3C',8)
	ht.printHashTable()
	print "------------------------------------------------"
	ht.putEntry('12:32:12:3C:2A:3C',9)
	ht.printHashTable()
	print "------------------------------------------------"
	ht.putEntry('13:3C:1B:3A:21:2B',9)
	ht.printHashTable()
	print "------------------------------------------------"


if __name__ == "__main__":
	main()