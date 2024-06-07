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
        # while low <= high:
        #     mid = (low + high) // 2
        #     left = mid - 1
        #     right = mid + 1 if mid + 1 < n else 0
        #     if nums[mid] <= nums[left] and nums[mid] <= nums[right]:
        #         return nums[mid]
            
        #     leftIsHigher = nums[left] < nums[mid] and nums[left] < nums[right]
        #     if leftIsHigher:
        #         high = mid - 1
        #     else:
        #         low = mid + 1
    # def findMin(self, nums: List[int]) -> int:
    #     self.dp(nums)
    #     return -1

    def dp(self, nums: List[int]):
        n = len(nums)
        if n <= 0:
            return -1
        if n == 1:
            return nums[0]
        low = 0
        high = n - 1
        mid = (low + high) // 2
        leftArr = nums[:mid+1]
        rightArr = nums[mid-1:]

        left = self.dp(leftArr)
        right = self.dp(rightArr)
        print(left, right)

sln = Solution()
# ans = sln.findMin([2,1py])
ans = sln.findMin([3,4,5,6,7,1,2])
# ans = sln.findMin([3,4,5,6,7,1,2])
print(ans)