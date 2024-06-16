from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProductSoFar = -float("inf")
        # negatives = 0
        # for num in nums:
        #     if num < 0:
        #         negatives += 1

        # if negatives % 2 == 0:
        #     product = 1
        #     for num in nums:
        #         product *= num
        #     return product
        # else:
        n = len(nums)

        for i in range(n):
            num1 = nums[i]
            product = num1
            maxProductSoFar = max(maxProductSoFar, num1)
            for j in range(i+1, n):
                num2 = nums[j]
                product *= num2
                maxProductSoFar = max(maxProductSoFar, product)

        return maxProductSoFar
    
sln = Solution()

# ans = sln.maxProduct([50,-3,5,-4,3,-5])
# ans = sln.maxProduct([0,0,0])
ans = sln.maxProduct([0,2])
print(ans)