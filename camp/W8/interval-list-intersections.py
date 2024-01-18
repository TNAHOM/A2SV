class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:

        output = []

        l, r = 0, 0
        while l< len(first) and r < len(second):
            print(first[l], second[r])
            if max(first[l][0], second[r][0]) <= min(first[l][1], second[r][1]):
                inter = max(first[l][0], second[r][0]), min(first[l][1], second[r][1])

                output.append(list(inter))

            if first[l][1] >= second[r][1]:
                r+=1
            else:
                l+=1
            
        
        return output