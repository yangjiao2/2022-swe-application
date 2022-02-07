
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
