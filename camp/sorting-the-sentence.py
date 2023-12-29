class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        output = [0 for _ in range(len(s))]

        for x in s:
            output[int(x[-1])-1] = x[:-1]

        return ' '.join(output)