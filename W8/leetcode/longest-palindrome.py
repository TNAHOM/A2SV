class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        value = list(count.values())

        value.sort(reverse=True)
        print(value)
        print(count)
        odd = 1
        output = 0

        for x in value:
            if x % 2 == 1 and odd ==1:
                odd-=1
                output+=x
            elif x%2 == 1 and odd <= 0:
                output+=x-1
            else:
                output+=x


        return output