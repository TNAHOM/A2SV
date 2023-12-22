class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        output = []

        for x in image:
            new = x[::-1]
            temp = []
            for y in new:
                if y == 0:
                    temp.append(1)
                else:
                    temp.append(0)
            output.append(temp)
        return output        