# 69. Sqrt(x)/


class Solution:
    def mySqrt(self, x: int) -> int:
        #         10 -> / 2   max 3
        #         100 -> / 3   max 10
        #         100 -> 4  max 31
        num_l = len(str(x)) if len(str(x)) % 2 == 0 else len(str(x)) - 1
        if num_l >= 2:
            left, right = 10 * (num_l - 2), x / num_l
        else:
            left, right = 0, 100
        while True:
            mid = left + (right - left) // 2
            if mid > x / mid:
                right = mid - 1
            else:
                if mid + 1 > x / (mid + 1):
                    return mid
                left = mid + 1
