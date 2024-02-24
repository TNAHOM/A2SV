class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        # print(count)
        output = 0

        for key, val in count.items():
            if key == 0:
                output+=val
            elif key+1 < val:
                same = val // (key+1)
                diff = val - (same*(key+1))
                output+=same*(key+1)
                if val % (key+1) != 0:
                    output+=key+1
            else:
                output+=key+1
        return output