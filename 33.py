from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            m = l + (r - l) // 2
            left, mid, right = nums[l], nums[m], nums[r]
            if target == mid:
                return m
            
            if left <= mid:
                if target < mid and target >= left:
                    r = m -1
                else:
                    l = m + 1
            else:
                if target > mid and target <= right:
                    l = m + 1
                else: 
                    r = m -1
            
                    
        return -1
    
sln = Solution()

tcs = [
    ([5,1,2,3,4], 5),
    ([3,1], 1),
    # ([1,2,3,4,5], 2),
    ([4,5,6,7,0,1,2], 4),
    ([4,5,6,7,8,1,2,3], 8),
    ([5,6,1,2,3,4], 6),
]

for tc in tcs:
    ans = sln.search(tc[0], tc[1])
    print(ans)