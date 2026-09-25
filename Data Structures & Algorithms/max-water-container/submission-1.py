class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights)-1
        maxWtr = 0


        while l < r:
            wtr = min(heights[l], heights[r]) * (r-l)
            maxWtr = max(wtr, maxWtr)


            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        
        return maxWtr
        