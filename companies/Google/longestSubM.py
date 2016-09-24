from heapq import heappush, heappop

def longestSubM(l, m):
	start = end = 0
	lengthL = len(l)
	mD   = {}
	cntD = {}

	while end<lengthL:
		while len(cntD)<m and end<lengthL:
			if l[end] not in cntD:
				cntD[l[end]]=1
			else:
				cntD[l[end]]+=1
			end+=1
		if end==lengthL:
			break

		mD[end-start+1]=start

		while len(cntD)==m:
			cntD[l[start]]-=1
			if cntD[l[start]]==0:
				del cntD[l[start]]
			start+=1

	maxSub = max(mD)
	return maxSub, mD[maxSub]

def main():
	l = 'adfadefcasedead'
	print longestSubM(l, 4)

if __name__=="__main__":
	main()