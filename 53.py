from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = 0
        max_ending_here = 0
        for num in nums:
            max_ending_here += num
            max_so_far = max(max_so_far, max_ending_here)
            max_ending_here = max(max_ending_here, 0)
        return max_so_far
        # pref_sum = []
        # n = len(nums)
        # pref_sum.append(nums[0])
        # for i in range(1, n):
        #     pref_sum.append(pref_sum[i-1] + nums[i])
        # # pref_sum.append(nums[n -])
        # max_sum = -1000000000
        # l, r = 0, n - 1
        # carry = 0
        # while l <= r:
        #     left, right = pref_sum[l], pref_sum[r] + carry
        #     max_sum = max(max_sum, right, right - left)
        #     # print(left, right)
        #     print(max_sum, right, right-left, carry)
        #     if left >= right:
        #         r -= 1
        #     if right >= left:
        #         l += 1
        #         carry -= nums[l]

        # print(pref_sum, max_sum)
        # return max_sum

sln = Solution()
# print(sln.maxSubArray([1,23,4,-56,4,79,0]))
# print(sln.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# print(sln.maxSubArray([5,4,-1,7,8]))
print(sln.maxSubArray([5,-1,5]))