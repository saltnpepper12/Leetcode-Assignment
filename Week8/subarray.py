class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maximumSum, currSumSubarray = float('-inf'), 0
        for i in range(n):
            currSumSubarray += nums[i]
            maximumSum = max(maximumSum, currSumSubarray)
            currSumSubarray = max(currSumSubarray, 0)
        return maximumSum
        