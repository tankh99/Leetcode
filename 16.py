from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        seen = set()
        min_diff = float("inf")
        ans = -1

        for i, num1 in enumerate(nums):
            j, k = i+1, n-1
            while j < k:
                num2 = nums[j]
                num3 = nums[k]
                sum = num1 + num2 + num3
                diff = abs(target - sum)
                if diff < min_diff:
                    ans = sum
                    min_diff = diff

                if sum > target:
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    return sum
        return ans
        

sln = Solution()
# [-4, -1, 1, 2]
ans = sln.threeSumClosest([0,0,0], 1)
print(ans)