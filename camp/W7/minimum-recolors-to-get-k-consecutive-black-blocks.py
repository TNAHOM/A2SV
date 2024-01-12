class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        output = float('inf')
        dic = defaultdict(int)

        l = 0
        for r in range(len(blocks)):
            dic[blocks[r]]+=1
            while dic['W'] + dic['B'] >= k:
                print(dic)
                output = min(output, dic['W'])
                dic[blocks[l]]-=1
                l+=1

        if output == inf:
            return blocks.count('W')
        return output