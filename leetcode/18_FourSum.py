"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.
Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        s = sorted(nums)
        sol = []
        length = len(nums)
        
        for m, num1 in enumerate(s[:-3]):
            #for n, num2 in enumerate(s[m+1:]):
            n=length
            while n>m+1:
                n-=1
                num2 = s[n]
                i=m+1
                j=n-1 #this is because n is starting its loop from 0
                
                while i<j:
                    num3 = s[i]
                    num4 = s[j]
                    q = [num1, num2, num3, num4]
                    
                    if sum(q)<target:
                        i+=1
                    elif sum(q)>target:
                        j-=1
                    else:
                        i+=1  #I think j-=1 might also work
                        sol.append(q)
        return sol