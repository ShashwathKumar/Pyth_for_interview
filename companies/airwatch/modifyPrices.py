def verifyItems(origItems, origPrices, items, prices):
	lengthOrig = len(origItems)
	i=0
	dOrig = {}
	while i<lengthOrig:
		dOrig[origItems[i]]=origPrices[i]
		i+=1

	cnt = 0
	i=0
	lenAlex = len(items)
	while i<lenAlex:
		if dOrig[items[i]]!=prices[i]:
			cnt+=1
		i+=1

	return cnt


