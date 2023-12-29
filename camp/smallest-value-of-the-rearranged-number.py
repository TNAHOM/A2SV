class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return 0
        tolist = list(str(num))
        zeros = []
        digit = []

        for x in tolist:
            if x != '-' and int(x)==0:
                zeros.append(x)
            elif x!= '-':
                digit.append(x)

        if tolist[0] == '-':
            sort_ = sorted(digit, reverse=True)
            output = sort_+zeros
            final = [str(x) for x in output if x!= ' ']
            return -int(''.join(final))
        else:
            sort_ = sorted(digit)
            output = list(str(sort_[0]))+zeros+sort_[1:]

            final = [str(x) for x in output if x!= ' ']
            return int(''.join(final))