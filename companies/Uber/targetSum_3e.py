def findElements(l, target):
	lengthL = len(l)
	combinations = []
	s = set(l[2])

	for i, num1 in enumerate(l[0]):
		for j, num2 in enumerate(l[1]):
			sumOf2 = num1 + num2
			if target-sumOf2 in s:
				combinations.append([num1, num2, target-sumOf2])
	return combinations

def main():
	l = [[1, 2, 3, 3], [2, 3, 3, 4], [1, 2, 2, 2]]
	target = 7
	print findElements(l, target)

if __name__ == "__main__":
	main()