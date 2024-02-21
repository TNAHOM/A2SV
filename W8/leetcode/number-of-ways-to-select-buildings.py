class Solution:
    def numberOfWays(self, s: str) -> int:
        s = list(map(int, s))

        count = Counter(s)
        count[s[0]]-=1
        check = {1:0, 0:0}
        check[s[0]]+=1

        output = 0
        s = s[1:]
        for x in s:
            count[x]-=1
            check[x]+=1

            if x == 1:
                if count[0] > 0 and check[0] > 0:
                    output+=(check[0] * count[0])

            elif x == 0:
                if count[1] > 0 and check[1] > 0:
                    output+=(check[1] * count[1])
            # print(x, output, check, count)
        # print(count, check)
        return output
