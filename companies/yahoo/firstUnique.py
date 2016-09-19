def firstUnique(l):
    d = {}
    s = set()
    cnt=1
    for v in l:
        if v not in s:
            if v not in d:
                d[v]=cnt
                cnt+=1
            else:
                del d[v]
                s.add(v)
    return min(d, key=d.get)

def main():
    l = 'abcaasdecb'
    print firstUnique(l)

if __name__ == "__main__":
    main()