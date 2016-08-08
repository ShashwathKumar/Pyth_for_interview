class HashMap(object):

	def __init__(self, key, value):
		self.l = [(None, None)]*101
		index = self.calc_hash(key)
		self.l[index] = (key, value)

	def __str__(self):
		return str(self.l)

	def get(self, key):
		index = self.calc_hash(key)
		return self.l[index][1]

	def put(self,key,value):
		index = self.calc_hash(key)
		self.l[index] = (key, value)

	def remove(self,key):
		index = self.calc_hash(key)
		self.l[index] = (None, None)

	def calc_hash(self, st):
		total = 0
		if(len(st)>0): total += ord(st[0])
		return total

def main():
	hm = HashMap('a',1)
	hm.put('b',2)
	print hm
	hm.put('c',3)
	hm.put('d',4)
	print hm
	print 'd: ',hm.get('d')
	hm.remove('c')
	print hm

if __name__ == "__main__":
	main()
