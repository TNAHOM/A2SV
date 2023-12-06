class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

        part_in = []
        output = []

        for x in range(len(words)):
            if words[x][0].lower() in row[0]:
                part_in.append(0)
            elif words[x][0].lower() in row[1]:
                part_in.append(1)
            elif words[x][0].lower() in row[2]:
                part_in.append(2)
        
        for y in range(len(words)):
            for z in words[y]:
                if z.lower() not in row[part_in[y]]:
                    break
            else:
                output.append(words[y])
        
        return output
        