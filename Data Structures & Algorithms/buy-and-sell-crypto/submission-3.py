class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        globMax = -1
        curMin = prices[0]

        for p in prices:
            globMax = max(p - curMin, globMax)
            curMin = min(p, curMin)
        
        return globMax
        