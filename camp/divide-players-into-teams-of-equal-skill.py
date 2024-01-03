class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        output = 0
        check = skill[0] + skill[-1]

        l = 0
        r=len(skill)-1
        while l < r:
            if skill[l] + skill[r] != check:
                return -1
            
            output+=skill[l]*skill[r]
            l+=1
            r-=1
        return output