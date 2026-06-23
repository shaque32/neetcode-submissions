class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        returnList = []
        for i in range(2):
            for n in nums:
                returnList.append(n)
        return returnList

        