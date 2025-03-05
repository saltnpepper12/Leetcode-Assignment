class Solution(object):
    def twoSum(self, numbers, target):
        left=0
        l=[]
        right=len(numbers)-1
        while(left<right):
            total=numbers[left]+numbers[right]
            if(total==target):
                return [left+1,right+1]
            elif total>target:
                right-=1
            else:
                left+=1
