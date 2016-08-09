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
		self.check_sTop()
		self.check_uTop()

	def getEntry(self, mac):
		hashIndex = self.calcHash(mac)
		return self.table[hashIndex]

	def putEntry(self, mac, port):
		hashIndex = self.calcHash(mac)

		newSlot = None
		if not self.table[hashIndex].entry[0]:  #this refers to mac address
		    #initializing newSlot variable for updation of sTop
			#update uTop - remove newSlot from the list of emptySlots
			if self.table[hashIndex]==self.uTop:
				self.uTop = self.uTop.nextEntry
			else:
				ptr = self.uTop
				while ptr.nextEntry != self.table[hashIndex]:
					ptr = ptr.nextEntry
				ptr.nextEntry = ptr.nextEntry.nextEntry
			self.table[hashIndex] = newSlot = HashEntry(mac, port)
		else:
			#handle collision
			#update uTop
			newSlot = self.uTop
			self.uTop = self.uTop.nextEntry
			newSlot.entry[0]=mac
			newSlot.entry[1]=port

			ptr = self.table[hashIndex]
			while ptr.entry[2]: #this refers to nextHashIndex
				newIndex = ptr.entry[2]
				ptr = self.table[newIndex]
			ptr.entry[2] = self.table.index(newSlot) #index of empty slot

		#update sTop
		if not self.sTop:
			self.sTop = newSlot
			self.sTop.nextEntry = None #This separates this entry from uTop
		else:
			ptr = self.sTop
			while ptr.nextEntry:
				#print ptr.nextEntry.entry
				ptr = ptr.nextEntry
			ptr.nextEntry = newSlot
			ptr.nextEntry.nextEntry = None

	def check_sTop(self):
		ptr = self.sTop
		print "************************************"
		print "filledSlots:"
		while ptr:
			#printing index here is inefficient but done just for visualization purposes
			print ptr.entry, self.table.index(ptr)
			ptr = ptr.nextEntry
		print "************************************"

	def check_uTop(self):
		ptr = self.uTop
		print "emptySlots:"
		while ptr:
			#printing index here is inefficient but done just for visualization purposes
			print ptr.entry, self.table.index(ptr) 
			ptr = ptr.nextEntry

	def calcHash(self, mac):
		macList = mac.split(':')
		hashIndex = int(macList[-1],16)%HTSize
		return hashIndex

	def clear(self):
		self.__init__()

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
	ht.clear()
	ht.printHashTable()
	print "------------------------------------------------"

if __name__ == "__main__":
	main()