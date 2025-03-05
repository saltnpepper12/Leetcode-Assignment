class Solution(object):
    def sortColors(self, nums):
        lower, middle, last = 0, 0, len(nums)-1
        while middle <= last:
            if nums[middle] == 0:
                nums[lower], nums[middle] = nums[middle], nums[lower]
                lower += 1
                middle += 1
            elif nums[middle] == 1:
                middle += 1
            else:
                nums[middle], nums[last] = nums[last], nums[middle]
                last -= 1
