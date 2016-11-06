#It worked for my test cases. I am not fully sure if it passes all test cases

def regex(s, p):
    j=0
    prevStar=None
    plength = len(p)
    for i,v in enumerate(s):
        if p[j]=='.':
            prevStar=None
            j+=1
        elif (p[j]=='*' or prevStar):
        	prevStar=1
        	if j!=plength-1 and p[j+1]==v:
        		prevStar=None
        		j+=1
        else:
            if not v==p[j]:
                return False
            j+=1
    return True

def main():
    s = 'ccca' #'abcd'
    p = 'c.ca'  #'a.*c'
    print regex(s,p)

if __name__ == "__main__":
    main()