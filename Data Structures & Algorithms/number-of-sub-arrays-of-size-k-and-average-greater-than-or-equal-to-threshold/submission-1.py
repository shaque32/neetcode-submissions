class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        curSum = 0
        count = 0
        targetVal = threshold * k

        for R in range(len(arr)):
            curSum += arr[R]

            if R-L+1 > k:
                curSum -= arr[L]
                L+=1

            if(R-L +1 ==k) and curSum >= targetVal:
                count += 1
            
        return count

       


            