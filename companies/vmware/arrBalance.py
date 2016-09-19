def  isArray_Balanced(arr):
    low  = 0
    high = len(arr)-1
    lSum = 0
    rSum = 0
    
    while low<=high:
        print low, high, lSum, rSum
        if lSum == rSum:
            if high==low:
                return low
            lSum += arr[low]
            rSum += arr[high]
            low +=1
            high-=1
        elif lSum > rSum:
            rSum += arr[high]
            high-=1
        else: 
            lSum += arr[low]
            low +=1
    return -1

def main():
    arr = [1,2,3,3]
    print isArray_Balanced(arr)

if __name__ == "__main__":
    main()