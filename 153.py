from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        n = len(nums)
        high = n - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[low]

sln = Solution()
# ans = sln.findMin([2,1py])
ans = sln.findMin([3,4,5,6,7,1,2])
# ans = sln.findMin([3,4,5,6,7,1,2])
print(ans)