class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0
        curWindow  = set()
        globMax = 0
        l=0

        for r in range(len(s)):
            while s[r] in curWindow:
                curWindow.remove(s[l])
                l+=1

                
            curWindow.add(s[r])
            globMax = max(r-l+1, globMax)
        
        return globMax

                



        