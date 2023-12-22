class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start_x, start_y = 0, 0
        stat = 0
        size = len(matrix)-1
        while start_y < (size+1)//2:
            first = start_x, start_y
            second = first[1], size - first[0]
            third = second[1], size - second[0]
            forth = third[1], size - third[0]

            matrix[first[0]][first[1]], matrix[second[0]][second[1]], matrix[third[0]][third[1]], matrix[forth[0]][forth[1]] = matrix[forth[0]][forth[1]], matrix[first[0]][first[1]], matrix[second[0]][second[1]], matrix[third[0]][third[1]]
            start_x+=1

            if start_x == size-stat:
                stat+=1
                start_x = stat
                start_y+=1