class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key= lambda x:x[1]-x[0])
        print(tasks)
        start = tasks[0][1]
        for x in range(1, len(tasks)):
            temp = start + tasks[x][0]
            start = max(temp, tasks[x][1])
        
        return start