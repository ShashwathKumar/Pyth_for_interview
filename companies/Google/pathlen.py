# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    # write your code in Python 2.7
    l = S.split('\n')
    levelSpaces = 0 #expected number of spaces at this level
    dirStack = []
    totalLen = 0
    
    for v in l:
        spaces = countSpaces(v)
        if not '.' in v:
            if spaces == levelSpaces:
                dirStack.append(v)
                levelSpaces+=1
            elif spaces==levelSpaces-1:
                dirStack.pop()
                dirStack.append(v)
            else:
                #dirStack.pop()
                #levelSpaces-=1
                #levelSpaces-=1
                levelDown = levelSpaces-spaces
                for i in xrange(levelDown):
                    dirStack.pop()
                dirStack.append(v)
                levelSpaces=spaces+1
        else:
            #reached an imgfile
            if v.endswith('jpeg') or v.endswith('png') or v.endswith('gif'):
                dirStack.append(v)
                totalLen += pathLen(dirStack)
                dirStack.pop()
    return totalLen

def pathLen(s):
    sNoSpace = map(lambda x: len(x.strip(' ')), s)
    sLen = reduce(lambda x,y: x+y, sNoSpace)
    return sLen+len(sNoSpace)

def countSpaces(s):
    spaceCount = 0
    for v in s:
        if v==' ':
            spaceCount+=1
        else:
            return spaceCount