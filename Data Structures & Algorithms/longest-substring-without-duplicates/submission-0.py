class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxLength = 0
        check = set()
        L = 0


        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[L])
                L +=1
            
            check.add(s[r])
            maxLength = max(r - L + 1, maxLength)
        
        return maxLength



        