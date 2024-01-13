class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        output = float('inf')
        dic = {}

        for x in range(len(cards)):
            if cards[x] in dic:
                output = min(output, (x-dic[cards[x]]+1))
                dic[cards[x]] = x
            else:
                dic[cards[x]] = x

        print(dic)
        if output == float('inf'):
            return -1
        return output