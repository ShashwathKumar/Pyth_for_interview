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
"""
This is an O(n^3) solution. But this can be improved by pruning off sums in early stages which can never reach the target sum
that means they are too small or too big
might have to keep track max 3 numbers and min 3 numbers for this
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        s = sorted(nums)
        length = len(nums)
        sol = {}
        q = []
        
        for m, num1 in enumerate(s[:-3]):
            n=length
            while n-1>m:
                n-=1
                num4 = s[n]
                i = m+1
                j = n-1
                while i<j:
                    num2, num3 = s[i], s[j]
                    q = [num1, num2, num3, num4]
                    print q, i, j, m, n
                    if sum(q) < target:
                        i+=1
                    elif sum(q) > target:
                        j-=1
                    else:
                        sol[str(q)] = q
                        i+=1
        return sol.values()

def main():
    o = Solution()
    l = [-2, 0, 0, -1, 2, 1]
    print o.fourSum(l, 0)

if __name__ == "__main__":
    main()