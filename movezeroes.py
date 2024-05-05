from typing import List


class Solution:
    def swap(self, nums: List[int], i: int, j: int):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    def moveZeroes(self, nums: List[int]) -> None:
        i = j = 0
        while i < len(nums) and j < len(nums):
            if nums[i] != 0:
                i += 1
            elif nums[j] != 0 and nums[i] == 0:
                self.swap(nums, i, j)
                i += 1
            j += 1

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == 0 and nums[j] != 0:
        #             self.swap(nums, i, j)
        print(nums)

sln = Solution()
a = [4,2,4,0,0,3,0,5,1,0]
sln.moveZeroes(a)
print(a)