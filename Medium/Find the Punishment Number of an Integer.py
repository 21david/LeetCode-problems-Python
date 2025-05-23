# See my LeetCode solution post -
# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/solutions/6423594/the-most-optimal-possible-solution-preco-l2oh/

# Actual algorithm
class Solution:
    def punishmentNumber(self, N: int) -> int:
        # Finds whether a number can be partitioned as described in the problem
        def can_partition(num):
            def helper(acc, n):
                if n <= 10:
                    return acc + n == num

                ans = False
                div = 10
                while (n * 10) // div:
                    ans |= helper(acc + n % div, n // div)
                    div *= 10

                return ans

            return helper(0, num**2)

        # Go through each number and add the squares of the numbers
        # that can be partitioned to the answer
        ans = 0
        for n in range(1, N + 1):
            if can_partition(n):
                ans += n ** 2

        return ans



# Precomputed numbers, assuming 1 <= n <= 1000
# TC: O(1)
# SC: O(1)
class Solution:
    def punishmentNumber(self, N: int) -> int:
        can_be_partitioned = [1,9,10,36,45,55,82,91,99,100,235,297,369,370,379,414,657,675,703,756,792,909,918,945,964,990,991,999,1000]

        ans = 0
        for num in can_be_partitioned:
            if num > N:
                break
            ans += num ** 2

        return ans



# Precomputed answers + quick retrieval with binary search
# TC: O(1)
# SC: O(1)
class Solution:
    def punishmentNumber(self, n: int) -> int:
        input = [1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000]
        output = [0, 1, 82, 182, 1478, 3503, 6528, 13252, 21533, 31334, 41334, 96559, 184768, 320929, 457829, 601470, 772866, 1204515, 1660140, 2154349, 2725885, 3353149, 4179430, 5022154, 5915179, 6844475, 7824575, 8806656, 9804657, 10804657]
        return output[bisect.bisect(input, n)]

