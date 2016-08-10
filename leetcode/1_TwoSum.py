class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        l = []
        for i,n in enumerate(nums):
            d[n]=i
        for j,n in enumerate(nums):
            if target-n in d:
                i = d[target-n]
                if i==j:
                    continue
                l.append(j)
                l.append(i)
                break
        return l