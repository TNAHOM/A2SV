class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}

        for x, y in enumerate(order):
            dic[y] = x
        
        for x in range(len(words)-1):
            for y in range(min(len(words[x]), len(words[x+1]))):
                if dic[words[x][y]] == dic[words[x+1][y]]:
                    continue

                if dic[words[x][y]] < dic[words[x+1][y]]:
                    break
                else:
                    return False   
            else:
                if len(words[x]) > len(words[x+1]):
                    return False

        return True