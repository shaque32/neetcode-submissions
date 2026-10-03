class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqS = {}
        freqt = {}

        for i in range(len(s)):
            freqS[s[i]]  = 1 + freqS.get(s[i], 0)
            freqt[t[i]] = 1 + freqt.get(t[i], 0)
        
        return freqS == freqt
        