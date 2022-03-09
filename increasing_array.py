class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        max_1, max_2 = 0, 0
        #  dp need to solve by forward[i] < num[i] < backward[i]


        for i in range(len(nums) - 1, 0, -1):
            print (max_1, max_2, i)
            if nums[i] >= max_1:
                max_1 = nums[i]
            elif nums[i] >= max_2:
                max_2 = nums[i]
            else:
                return True


        return False
