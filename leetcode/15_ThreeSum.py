class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        length = len(nums)

        for i,n1 in enumerate(nums):
            for j,n2 in enumerate(nums[i+1:length]):
                for k, n3 in enumerate(nums[i+2+j:length]):
                    if i==8:
                        print n1,n2,n3
                    if n1+n2+n3==0:
                        triplet = [n1, n2, n3]
                        if not self.combInL(l, triplet):
                            l.append(triplet)
        return l
        
    def combInL(self, l, triplet):
        for comb in l:
            s = set(comb)
            for n in triplet:
                if all(map(lambda x: x in s, triplet)):
                    return True
        return False

def main():
    o = Solution()
    print o.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])

if __name__ == "__main__":
    main()














class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        length = len(nums)

        for i,n1 in enumerate(nums):
            for j,n2 in enumerate(nums[i+1:length]):
                for k, n3 in enumerate(nums[i+2+j:length]):
                    if n1+n2+n3==0:
                        triplet = [n1, n2, n3]
                        if not self.combInL(l, triplet):
                            l.append(triplet)
        return l
        
    def combInL(self, l, triplet):
        for comb in l:
            s = set(comb)
            for n in triplet:
                if all(map(lambda x: x in s, triplet)):
                    return True
        return False