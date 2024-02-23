class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        ans = [0 for _ in range(size)]
        stack = [(temperatures[-1], size-1)]

        for x in range(size-2, -1, -1):
            while stack and stack[-1][0] <= temperatures[x]:
                stack.pop()
            
            if stack:
                ans[x] = stack[-1][1] - x
            stack.append((temperatures[x],x))
            
        return ans