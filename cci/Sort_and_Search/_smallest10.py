#this is an imp question. practice this properly.

def swap(l, i, j):
    if i!=j:
        l[i], l[j] = l[j], l[i]
    return l

def partition(l, low, high):
    print l, low, high
    j=low
    pivot = l[high]
    for i, n in enumerate(l[low:high]):
        if n <= pivot:
            l = swap(l, i, j)
            j+=1
    swap(l, -1, j)
    return l, j+low

def smallest10(l):
    low  = 0
    high = len(l)-1
    k = 10
    j=-1

    while True:  #j is in index and k is in numbers
        l, j = partition(l, low, high)
        if j==k-1:
            break
        if k<j:
            high=j-1
        else:
            low =j+1

    return l[:k]

def main():
    l = [1, 5, 3 ,2 ,4, 7, 9, 8, 0, 10, 14, 11, 12]
    print l
    print smallest10(l)

if __name__ == "__main__":
    main()