class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(Counter(fruits)) == 1:
            return len(fruits)
        exist = {}
        output = 0
        l = 0
        for r in range(len(fruits)):
            exist[fruits[r]] = exist.get(fruits[r], 0)+1
            if len(exist) == 2:
                output = max(output, r-l+1)
            
            while len(exist) > 2 :
                exist[fruits[l]]-=1
                if exist[fruits[l]] == 0:
                    del exist[fruits[l]]
                l+=1

        return output