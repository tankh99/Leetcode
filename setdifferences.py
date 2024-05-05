# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Better answer
        set1, set2 = set(nums1), set(nums2)
        return [list(set1-set2), list(set2-set1)]

        # Original answer
        # seen = set()
        # common = set()
        # for num in nums1:
        #     seen.add(num)

        # for num in nums2:
        #     if num in seen:
        #         common.add(num)

        # uncommon1 = set()
        # for num in nums1:
        #     if num not in common:
        #         uncommon1.add(num)

        # print(common)
        # uncommon2 = set()
        # for num in nums2:
        #     if num not in common:
        #         uncommon2.add(num)

        # return [list(uncommon1), list(uncommon2)]
    
sln = Solution()
ans = sln.findDifference([1,2,3], [4,6,9,12])
print(ans)