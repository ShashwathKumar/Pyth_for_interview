
class Multi(object):

	def __init__(self, l):
		self.myList = []
		self.myList.append(l[0])
		self.myList.append(self.first(l[1]))
		self.myList.append(self.second(l[2]))
		self.myList.append(l[3])
		self.myList.append(l[4])
		self.myList.append(l[5])

	def first(self, num):
		l=[]
		l.append(num)
		return l

	def second(self, num):
		l1=[]
		l2=[]
		l3=[]
		l3.append(num)
		l2.append(l3)
		l1.append(l2)
		return l1

	def getMyList(self):
		return self.myList

def implementMulti(l):
	var = Multi(l)
	return var.getMyList()

def main():
	l = [1,2,3,4,5,6]
	print implementMulti(l)

if __name__ == "__main__":
	main()