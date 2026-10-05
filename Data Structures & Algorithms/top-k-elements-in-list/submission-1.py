class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = {}
        count = {}

        for n in nums:
            freqList[n] = freqList.get(n,0) + 1

        counts = [[] for _ in range(len(nums)+1)]
        for num, val in freqList.items():
            counts[val].append(num)
        res = []
        for freq in range(len(counts)-1,0,-1):
            for n in counts[freq]:
                res.append(n)
            
            if len(res) == k: return res
                   





        

        