class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        pref=[1]*n
        suff=[1]*n
        answer=[0]*n
        for i in range(1,n):
            pref[i]=nums[i-1]*pref[i-1]
        for i in range(n-2,-1,-1):
            suff[i]=nums[i+1]*suff[i+1]
        for i in range(n):
            answer[i]=suff[i]*pref[i]
        return answer