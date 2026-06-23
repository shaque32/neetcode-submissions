class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkList = set(nums)
        return (len(checkList) < len(nums))

         