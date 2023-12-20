class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        output = 0

        for x in range(len(strs[0])):
            for y in range(len(strs)-1):
                if strs[y][x] > strs[y+1][x]:
                    output+=1
                    break

        return output