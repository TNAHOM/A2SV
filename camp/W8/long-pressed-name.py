class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0

        while i < len(typed) and j < len(name):
            if typed[i] == name[j]:
                i += 1
                j += 1
            elif i > 0 and typed[i] == typed[i - 1]:
                i += 1
            else:
                return False

        while i < len(typed):
            if typed[i] != typed[i - 1]:
                return False
            i += 1

        return j == len(name)
        