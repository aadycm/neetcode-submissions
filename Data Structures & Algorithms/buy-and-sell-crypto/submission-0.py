class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=0
        b=1
        maxp=0
        while b < len(prices):
            if prices[b] > prices[a]:
                p = prices[b] - prices[a]
                maxp = max(maxp,p)
            else:
                a = b
            b+=1
        return maxp        