class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMin = 0
        curMax = 0
        maxMin = nums[0]
        maxMax = nums[0]
        total = 0

        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total+=n


            maxMax = max(curMax, maxMax)
            maxMin= min(curMin, maxMin)
        

        if maxMax < 0:
            return maxMax
        else:
            return max(total - maxMin, maxMax)
        