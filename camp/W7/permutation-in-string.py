class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_dic = Counter(s1)
        s2_dic = {}
        
        l = 0
        for r in range(len(s2)):
            if s2[r] in s1_dic:
                s2_dic[s2[r]] = s2_dic.get(s2[r], 0)+1
            if s1_dic == s2_dic:
                return True
            
            while len(s1) <= r-l+1:
                print(s2[r], s2_dic)
                if s2[l] in s2_dic:
                    s2_dic[s2[l]]-=1
                l +=1
                

        return False