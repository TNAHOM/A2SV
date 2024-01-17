class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        print(-30%-26)
        temp = [0 for _ in range(len(s)+1)]

        for l, r, k in shifts:
            if k == 1:
                temp[l]+=1
                temp[r+1] -=1
            else:
                temp[l]-=1
                temp[r+1]+=1
        # print(temp)  
        output = ''
        curr = 0

        for x in range(len(s)):
            curr += temp[x]
            # print(curr)

            char_ord = ord(s[x])+(curr)%(-26 if curr < 0 else 26)

            # print(char_ord)

            if char_ord > 122:
                char_ord = 97 + ((char_ord % 122)-1)
            elif char_ord < 97:
                char_ord = 122 - ((97%char_ord))+1
            # print(char_ord, chr(char_ord))

            output = output+chr(char_ord)


        return output

        
