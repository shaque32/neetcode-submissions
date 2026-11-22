class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        valToIndex = {}
        res = []

        for i in range(len(nums2)):
            valToIndex[nums2[i]] = i

        for num in nums1:
            res.append(valToIndex[num])

        return res

        

        