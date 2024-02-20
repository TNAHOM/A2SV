class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        check = Counter(s)
        list_ = set()
        last = -1
        output = []

        for ind,x in enumerate(s):
            check[x]-=1
            list_.add(x)
            if check[x] == 0:
                list_.discard(x)
            
            if len(list_) == 0:
                output.append(ind-last)
                last = ind
        
        return output
