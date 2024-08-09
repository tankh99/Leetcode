from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def is_magic_square(r, c):
            square = [row[c:c + 3] for row in grid[r:r+3]]
            seen = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

            for i in range(3):
                for j in range(3):
                    num = square[i][j]
                    
                    '''
                    multiple conditions:
                    1. unique numbers from 1 to 9
                    2. every row, col and diagonal have same sum
                    '''
                    if num in seen and seen[num] == 0:
                        seen[num] += 1
                    else:
                        return False

            #  check rows
            row_sum = -1
            for i in range(3):
                row = square[i]
                if row_sum == -1:
                    row_sum = sum(row)
                if row_sum != sum(row):
                    return False
                
            # Check cols
            col_sum = -1
            for i in range(3):
                col = [row[i] for row in square]
                if col_sum == -1:
                    col_sum = sum(col)
                
                if col_sum != sum(col):
                    return False

            diag_sum = -1
            top_left, top_left_dir = (r,c), (1,1)
            for i in range(3):
                r_coord, c_coord = top_left
                dir_r, dir_c = top_left_dir
                if diag_sum == -1:
                    diag_sum = 0
                
                diag_sum += grid[r_coord][c_coord]
                top_left = (r_coord + dir_r, c_coord + dir_c)

            bottom_left, bottom_left_dir = (r+2,c), (-1,1)
            for i in range(3):
                r_coord, c_coord = bottom_left
                dir_r, dir_c = bottom_left_dir
                if diag_sum == -1:
                    diag_sum = 0
                
                diag_sum -= grid[r_coord][c_coord]
                bottom_left = (r_coord + dir_r, c_coord + dir_c)

            return diag_sum == 0

        magic_count = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if is_magic_square(i, j):
                    magic_count += 1
        return magic_count
    

sln = Solution()
# arr = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
arr = [[2,7,6,9],[9,5,1,6],[4,3,8,8],[1,4,10,1]]
# print(arr[0:2][0])
ans = sln.numMagicSquaresInside(arr)
print(ans)
