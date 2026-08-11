class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        L = 0
        total = 0
        minLength = len(nums)+1

        for r in range(len(nums)):
            total += nums[r]

            while (total >= target):
                minLength = min(minLength, r-L+1)
                total -= nums[L]
                L+=1


        if minLength == len(nums)+1:
            return 0
        else:
            return minLength


        