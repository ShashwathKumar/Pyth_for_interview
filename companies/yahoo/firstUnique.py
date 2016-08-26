def firstUnique(l):
    d = {}
    cnt=1
    for v in l:
        if v not in d:
            d[v]=cnt
            cnt+=1
        else:
            del d[v]
    return min(d, key=d.get)

def main():
    l = 'abcasdecb'
    print firstUnique(l)

if __name__ == "__main__":
    main()