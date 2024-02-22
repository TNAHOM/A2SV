class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for x in logs:
            if stack and x == '../':
                stack.pop()
            elif x != './' and x!= '../':
                stack.append(x)
        
        return len(stack)
