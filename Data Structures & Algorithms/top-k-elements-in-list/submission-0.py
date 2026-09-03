class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #creating a frequency list for each number in nums
        #we populate a count map by looping through nums 
        #we then update our frequency table by adding all numbs with same count to the same key
        #we loop through the nums in the freq of i going backwords and append to a result list until our list equals the k values
        count ={}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1+count.get(n,0)
        
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq)-1, 0 ,-1):
            for nums in freq[i]:
                res.append(nums)
                if len(res) == k:
                    return res





        

        