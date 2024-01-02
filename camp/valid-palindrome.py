class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = [x.lower() for x in s if x.isalnum() == True]
        new = ''.join(new)
       
        l = 0
        r = len(new)-1
        print(new)
        while l < r:
            if new[l] != new[r]:
                return False
            l+=1
            r-=1
        return True