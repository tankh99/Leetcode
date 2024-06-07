from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1 # There must be at least 1 unit spacing between l and r
        maxArea = 0
        while l < r:
            area = self.getArea((l, height[l]), (r, height[r]))
            maxArea = max(maxArea, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea

    def dp(self, height: List[int], memo, left, right):
        if left == right:
            right += 1
        if left > right or right >= len(height):
            return 0
        
        if memo[left] != 0 or memo[right] != 0:
            return max(memo[left], memo[right])
        
        # self.getArea
        lCoord = (left, height[left])
        rCoord = (right, height[right])
        area = self.getArea(lCoord, rCoord)
        maxArea = max(area, self.dp(height, memo, left, right + 1), self.dp(height, memo, left + 1, right))
        memo[left] = maxArea
        memo[right] = maxArea
        return maxArea
    
    # def dp(self, height: List[int]):
        # n = len(height)
        # dp = [0 for _ in range(n)]
        # dp[0] = 0
        # for i in range(1, n):
        #     for j in range(i):
        #         dp[i] = max(dp[i], self.getArea((j, height[j]), (i, height[i])))
        # return dp
    
    def getArea(self, c1, c2):
        x1, y1 = c1
        x2, y2 = c2

        x = x2 - x1
        y = min(y1, y2)
        return x * y

sln = Solution()
ans = sln.maxArea([1,8,6,2,5,4,8,3,7])
# ans = sln.maxArea([76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191])
# ans = sln.maxArea([2,3,4,5,18,17,6])
# ans = sln.maxArea([1,1])
print(ans)