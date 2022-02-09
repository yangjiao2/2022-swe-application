class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums) - 1
        start, end = [1, n - 1]
        forward_d = {0: nums[0]}
        backward_d = {n: nums[n]}
        while start < end:
            forward_d[start] = forward_d[start - 1] + nums[start]
            backward_d[end] = backward_d[end + 1] + nums[end]
            start += 1
            end -= 1
        mid = 0
        if start == end:
            mid = nums[start]
        total = start + end + mid

        start, end = [0, n]
        res = 0
        # print (start,mid,  end, forward_d , backward_d)
        while start < end and start < mid and mid < end:
            mid_range = total - forward_d[start] - backward_d[end]
            if forward_d[start] <= mid_range and backward_d[end] >= mid_range:
                res += 1
            print(start, end, forward_d[start], mid_range, backward_d[end])
            if forward_d[start] >= backward_d[end]:
                end -= 1
            elif forward_d[start] <= backward_d[end]:
                if forward_d[start] >= mid_range:
                    mid -= 1
                elif backward_d[end] <= mid_range:
                    end -= 1
            else:
                start += 1

        return res


# class Solution:
#     def waysToSplit(self, nums: List[int]) -> int:
#         count = 0
#         n = len(nums)
#         left1 = left2 =  0
#         overall_sum = right_sum = sum(nums)
#         mid_sum1 = mid_sum2 = 0
#         for i in range(1, n):
#             right_sum -= nums[i - 1]
#             mid_sum1 += nums[i - 1]
#             mid_sum2 += nums[i - 1]
#             while left1 < i and mid_sum1 > right_sum:
#                 mid_sum1 -= nums[left1]
#                 left1 += 1
#             while left2 < i and overall_sum - mid_sum2 - right_sum <= mid_sum2:
#                 mid_sum2 -= nums[left2]
#                 left2 += 1

#             if left2 > left1:
#                 count += left2 - max(1, left1)


#         return count
