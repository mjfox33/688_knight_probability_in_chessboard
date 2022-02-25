class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k < 1:
            return 1
        
        if n < 3:
            return 0

        move_xy = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        dp = [[ [0]*(k+1) for _ in range(n)] for _ in range(n)]

        def is_move_valid(row, col):
            return row >=0 and row < n and col >=0 and col < n

        def get_valid_moves(k, row, col):
            if not is_move_valid(row,col):
                return 0

            if k==0:
                return 1

            if dp[row][col][k] != 0:
                return dp[row][col][k]

            rate = 0
            for i in range(8):
                rate += 0.125 * get_valid_moves(k-1, row+move_xy[i][0], col+move_xy[i][1])
            dp[row][col][k] = rate
            return rate
        
        result = get_valid_moves(k, row, column)
        return result