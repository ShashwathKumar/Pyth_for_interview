"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
    For example, given array S = {-1 2 1 -4}, and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Subscribe to see which companies asked this question

Show Tags
Show Similar Problems
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s = sorted(nums)
        length = len(nums)
        sol = sys.maxint
        currDiff = target + 10000 #taking currSum away from required target
        
        for n, num1 in enumerate(s[:-2]):
            i = n+1
            j = length-1
            while i<j:
                num2 = s[i]
                num3 = s[j]
                l = [num1, num2, num3]
                if sum(l) > target:
                    j-=1
                    if abs(sum(l)-target) < currDiff:
                        sol = sum(l)
                        currDiff = abs(sol-target)
                elif sum(l) < target:
                    i+=1
                    if abs(sum(l)-target) < currDiff:
                        sol = sum(l)
                        currDiff = abs(sol-target)
                else:
                    sol = sum(l)
                    return sol
        return sol