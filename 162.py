from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print(l, r)
            if self.isPeak(nums, mid):
                return mid
            
            if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                r = mid-1
            elif mid + 1 < len(nums) and nums[mid + 1] > nums[mid]:
                l = mid+1
        return mid
        
    def isPeak(self, nums, mid):
        leftIndex = mid - 1
        rightIndex = mid + 1
        num = nums[mid]
        if (mid + 1) >= len(nums) and num > nums[mid-1]: return True
        if (mid - 1) <= -1 and num > nums[mid + 1]: return True
        if (mid - 1) <= -1 or (mid + 1) >= len(nums): return False
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]: return True
        # if leftIndex <= -1 and nums[mid] > nums[rightIndex]:
        #     return True
        # if rightIndex >= len(nums) and nums[mid] > nums[leftIndex]:
        #     return True
        # if leftIndex < 0 or rightIndex >= len(nums):
        #     return False
        # if nums[mid] > nums[leftIndex] and nums[mid] > nums[rightIndex]:
        #     return True
        return False

sln = Solution()
ans = sln.findPeakElement([1, 2])
print(ans)
# sln.totalCost([1,2,4,1], 3, 4)