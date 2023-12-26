class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashmap = {}
        for x in arr2:
            if x not in hashmap:
                hashmap[x] = 0
        
        none = []
        for x in arr1:
            if x in hashmap:
                hashmap[x]+=1
            else:
                none.append(x)
        none.sort()
        output = []
        for key, value in hashmap.items():
            for y in range(value):
                output.append(key)

        if len(none) == 0:
            return output
        else:
            return output + none

