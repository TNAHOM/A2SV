class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        status = {}

        for x in cpdomains:
            sep = x.split()
            for y in range(len(sep[1])-1, 1,-1):
                if sep[1][y] == '.':
                    status[sep[1][y+1:]] = status.get(sep[1][y+1:], 0) + int(sep[0])
            status[sep[1]] = status.get(sep[1], 0) + int(sep[0])
            
        output = []
        for key, value in status.items():
            output.append(str(str(value) +' '+ key))
        return output