class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(heights)
        
        for x in range(size):
            min_val = x
            for y in range(x+1, size):
                if heights[min_val] < heights[y]:
                    min_val = y
            
            if min_val != x:
                heights[x], heights[min_val] = heights[min_val], heights[x]
                names[x], names[min_val] = names[min_val], names[x]
        
        return names

