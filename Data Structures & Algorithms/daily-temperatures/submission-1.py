class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #array of ints temps where i represents temp on ith day
        #return res array where res[i] is num days after ith day before warmer temp appears on future day

        res = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        
        return res
