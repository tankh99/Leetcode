from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n % 2 == 0:
            for i in range(1, n//2 + 1):
                ans.append(i)
                ans.append(-i)
        else:
            if n >= 3:
                for i in range(4, (n - 3) // 2 + 4):
                    ans.append(i)
                    ans.append(-i)
                ans.append(1)
                ans.append(2)
                ans.append(-3)
            else:
                ans.append(0)
        return ans

sln = Solution()
ans = sln.sumZero(1)
print(ans)