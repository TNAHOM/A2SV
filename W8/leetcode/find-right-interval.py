class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        first = [x[0] for x in intervals]
        first.sort()

        stat = {}
        for x in range(len(intervals)):
            stat[intervals[x][0]] = x
        ans = []

        for start, end in intervals:
            
            temp = bisect_left(first, end)

            if temp<len(intervals):
                ans.append(stat[first[temp]])
            else:
                ans.append(-1)

        return ans