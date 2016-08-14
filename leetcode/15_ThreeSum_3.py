"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = sorted(nums)
        length = len(nums)
        sol={}    #purpose of dictionary is not to repeat the entries
        print s
        for n, num1 in enumerate(s[:-2]):
            i = n+1
            j = length-1
            while i<j:
                num2 = s[i]
                num3 = s[j]
                print num1, num2, num3, sol.values()
                sum = num1+num2+num3
                if sum > 0:
                    j-=1
                elif sum<0:
                    i+=1
                else:
                    sol[str([num1, num2, num3])] = [num1, num2, num3]
                    j-=1  #here, i+=1 will also work
        return sol.values()
        
def main():
    o = Solution()
    l = [-2, -1, 0, 2, 1, 3]
    print o.threeSum(l)

if __name__ == "__main__":
    main()