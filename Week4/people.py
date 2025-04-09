class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        dp = [0]*n
        dp[0]=1
        ppl = 0

        for today in range(delay,n):
            ppl += dp[today-delay]
            dp[today] = ppl
            if today-forget+1 >=0:
                ppl -= dp[today-forget+1]
        return sum(dp[-forget::])%(10**9+7)
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        
