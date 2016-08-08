

def checkOrder(inputo, ordering):
	ordIndex = 0
	ordLen   = len(ordering)

	for c in inputo:
		if c == ordering[ordIndex]:
			ordIndex+=1
			if ordIndex == ordLen:
				return True
	return False

def main():
	inputo = 'hello world!'
	ordering = 'hlo!'
	print checkOrder(inputo, ordering)

if __name__ == "__main__":
	main()