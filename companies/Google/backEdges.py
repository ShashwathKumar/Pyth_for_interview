def backEdges(G, start):
	stack     = []
	backEdges = []
	stack.append(start)

	while stack:
		curr = stack.pop()
		for node in G[curr.name]:
			if node in curr.parents:
				backEdges.append(curr.name+node.name)
			elif not node.visited:
				node.parents.add(curr)
				node.visited=True
				stack.append(node)
	return backEdges

class Node(object):
	def __init__(self, name):
		self.name = name
		self.visited  = False
		self.parents  = set()

def getGraph():
	G = {}
	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')
	e = Node('e')
	f = Node('f')
	g = Node('g')

	G['a']=[b, c]
	G['b']=[g, f]
	G['c']=[e, d]
	G['d']=[c]
	G['e']=[b, f]
	G['f']=[]
	G['g']=[b, f]

	return G, a

def main():
	G, start = getGraph()
	print backEdges(G, start)

if __name__ == "__main__":
	main()