class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output = []
        dic_check = {}
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if y+x in dic_check.keys():
                    dic_check[y+x].append(mat[x][y])
                else:
                    dic_check[y+x] = []
                    dic_check[y+x].append(mat[x][y])

        for key, value in dic_check.items():
            if key%2 == 0 and key !=0:
                output.extend(dic_check[key][::-1])
            else:
                output.extend(dic_check[key])

        return output
