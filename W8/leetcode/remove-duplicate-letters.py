class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_occ = defaultdict(int)
        seen = set()

        for ind, val in enumerate(s):
            last_occ[val] = ind
        
        for x in range(len(s)):
            if s[x] in seen: continue

            while stack and (stack[-1] > s[x] and last_occ[stack[-1]] > x):
                seen.discard(stack.pop())

            stack.append(s[x])
            seen.add(s[x])
        return ''.join(stack)
