class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        max_ = 0
        for x in range(3, len(tasks), 4):
            print(x, ((x+1)//4))
            max_ = max(max_, tasks[x] + processorTime[-((x+1)//4)])
        return max_