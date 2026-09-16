class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])


        res = []
        curRange = [intervals[0][0],intervals[0][1]]

        for i in range(len(intervals)):

            start = intervals[i][0]
            end = intervals[i][1]

            if(start <= curRange[1]):
                curRange[1] = max(curRange[1], end)
                continue
            if (start > curRange[0]):
                res.append(curRange)

            curRange = [start, end]
        res.append(curRange)
        return res

        