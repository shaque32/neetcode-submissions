class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #array of ints temps where i represents temp on ith day
        #return res array where res[i] is num days after ith day before warmer temp appears on future day

        res = [0]*len(temperatures)
        stack = []


        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, StackInd = stack.pop()
                res[StackInd] = (i - StackInd)
            stack.append([t,i])
        return res


        
