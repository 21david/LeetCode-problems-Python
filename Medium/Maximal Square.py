# https://leetcode.com/problems/maximal-square/description/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        R = len(matrix)
        C = len(matrix[0])
        dp = [[0] * C for _ in range(R)]

        def in_bounds(r, c):
            return 0 <= r < R and 0 <= c < C

        max_length = 0

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == '0':
                    continue

                square1 = dp[r-1][c] if in_bounds(r-1,c) else 0
                square2 = dp[r-1][c-1] if in_bounds(r-1,c-1) else 0
                square3 = dp[r][c-1] if in_bounds(r,c-1) else 0

                dp[r][c] = min(square1, square2, square3) + 1
                max_length = max(max_length, dp[r][c])

        return max_length**2


'''
Same solution, but written shorter.
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        R = len(matrix)
        C = len(matrix[0])
        dp = [[0] * C for _ in range(R)]
        max_len = 0
        
        for r, c in product(range(R), range(C)):
            if matrix[r][c] == '1':
                try:
                    sq1 = dp[r-1][c]
                    sq2 = dp[r-1][c-1]
                    sq3 = dp[r][c-1]
                except IndexError:
                    sq1 = 0
                
                dp[r][c] = min(sq1, sq2, sq3) + 1
                max_len = max(max_len, dp[r][c])
                
        return max_len**2
