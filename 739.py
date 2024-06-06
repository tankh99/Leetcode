from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        stack.append(0)
        answer = [0 for _ in range(len(temperatures))]
        for i in range(1, len(temperatures)):
            if not stack:
                stack.append(i)
                continue

            # print(stack)
            while stack and temperatures[stack[-1]] < temperatures[i]:
                popped = stack.pop()
                answer[popped] = i - popped

            stack.append(i)
        return answer
        # print(answer, stack)

sln = Solution()

ans = sln.dailyTemperatures([73,74,75,71,69,72,76,73])
print(ans)