class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}

        for x in paths:
            x = x.split()
            for y in range(1, len(x)):
                content = x[y].split('(')[1][:-1]
                item = x[0]+'/'+x[y].split('(')[0]
                if content in dic:
                    dic[content].append(item)
                else:
                    dic[content] = [item]
        
        return [display for display in dic.values() if len(display) > 1]