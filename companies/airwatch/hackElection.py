from collections import Counter

def electionWinner(votes):
	c = Counter(votes)
	maxCnt = max(c.values())
	winner = 'A'
	for k,v in c.items():
		if v==maxCnt and k>=winner:
			winner=k
	return winner