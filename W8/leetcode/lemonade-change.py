class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {}

        for x in bills:
            temp = x-5
            if temp in change:
                change[temp] = change.get(temp, 0)-1
                change[x] = change.get(x, 0)+1
            elif temp == 15:
                if 10 in change and 5 in change and change[10] > 0 and change[5] >= 1:
                    change[10]-=1
                    change[5]-=1
                elif 5 in change and change[5] >= 3:
                    change[5]-=3
                else:
                    return False
            elif temp == 0:
                change[5] = change.get(5, 0)+1
            else:
                return False

            
            print(change)
        return True