class Stack(object):
	def __init__(self):
		self.enqS = []
		self.deqS = []

	def enque(self, n):
		self.enqS.append(n)

	def deque(self):
		if not self.deqS:
			while self.enqS:
				self.deqS.append(self.enqS.pop())
		if self.deqS:
			return self.deqS.pop()

def main():
	s = Stack()
	s.enque(1)
	s.enque(2)
	s.enque(3)
	for n in xrange(3):
		print s.deque()
	s.enque(4)
	s.enque(5)
	s.enque(6)
	for n in xrange(3):
		print s.deque()

if __name__ == "__main__":
	main()