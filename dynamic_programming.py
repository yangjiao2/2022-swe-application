# 2140. Solving Questions With Brainpower
# https://leetcode.com/problems/solving-questions-with-brainpower/
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        res = [0] * (n + 1)
        res[n] = questions[n - 1][0]

        for i in range(n - 1, -1, -1):
            print(i)
            print(res)
            pts, step = questions[i]
            if i + step >= n - 1:
                res[i] = max(res[i + 1], pts)
            else:
                res[i] = max(res[i + 1], pts + res[i + step + 1])
        return res[0]


# Thinking process:
# - 从后往前: panelty/ contraints 是 skipped step
# - max on list 可以简单完成单调递增累计
# - base case: choose current + future / not choose, keep previous


# 1937. Maximum Number of Points with Cost
# https://leetcode.com/problems/maximum-number-of-points-with-cost/


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        col_n = len(points[0])
        row_n = len(points)
        for r in range(1, row_n):
            for c1 in range(col_n):
                cur_max = 0

                for c2 in range(col_n):
                    cur_max = max(
                        cur_max, points[r][c1] + points[r - 1][c2] - abs(c2 - c1)
                    )

                points[r][c1] = cur_max
            print(points)
        return max(points[row_n - 1])

    def maxPoints_Sol(self, points):
        dp = [
            0 for i in range(len(points[0]))
        ]  # each dp[c] means the max val points[r][c] can get from previous row
        for r in range(len(points)):
            dp[0] += points[r][0]
            print(dp)
            for c in range(1, len(points[0])):  # forward pass
                dp[c] = max(dp[c] + points[r][c], dp[c - 1] - 1)
            for c in range(len(points[0]) - 2, -1, -1):  # backward pass
                dp[c] = max(dp[c], dp[c + 1] - 1)
        return max(dp)


# Thinking process:
# - increasing by row
# - keep record of largest: 每个cell 对于当然 row x col 最大值
#   - 从左到右 遍历， 每个减去panelty
#   - 从右到左 遍历， 每个减去panelty
