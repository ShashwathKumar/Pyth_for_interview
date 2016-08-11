"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

#this code seems to work but is very slow -- Time limit exceeded
import collections

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
            if collections.Counter(comb)==collections.Counter(triplet):
                return True
        return False
   
def main():
    o = Solution()
    print o.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])

if __name__ == "__main__":
    main()