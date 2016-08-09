class Node(object):
	def __init__(self, data):
		self.data = data
		self.nextPtr = None

class LL(object):
	def __init__(self, n=None): #let n be some integer
		self.top = Node(n)

	def printList(self):
		ptr = self.top
		while ptr:
			print ptr.data
			ptr = ptr.nextPtr

	def insertBeg(self, n):
		newNode = Node(n)
		newNode.nextPtr = self.top
		self.top = newNode

def main():
	myList = LL(1)
	myList.insertBeg(2)
	myList.printList()

if __name__ == "__main__":
	main()