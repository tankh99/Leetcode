from typing import List
import numpy as np
import heapq

"""

"""

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # n = len(costs)
        # leftheap = []
        # rightheap = []
        # firstGroup = costs[:candidates]
        # secondGroup = costs[n-candidates:]
        # for i in range(candidates):
        #     heapq.heappush(leftheap, (firstGroup[i], i))
        #     heapq.heappush(rightheap, (secondGroup[i], n-candidates+i))
        # totalCost = 0
        # leftpoppedcount = 0
        # rightpoppedcount = 0
        # for i in range(k):
        #     left, lefti = leftheap[0]
        #     right, righti = rightheap[0]
        #     newlefti = candidates + leftpoppedcount
        #     newrighti = n - candidates - 1 - rightpoppedcount
        #     if left < right:
        #         totalCost += left
        #         heapq.heappop(leftheap)
        #         # costs.remove(left)
        #         heapq.heappush(leftheap, (costs[newlefti], newlefti))
        #         leftpoppedcount += 1
        #     elif right < left:
        #         totalCost += right
        #         # costs.remove(right)
        #         heapq.heappop(rightheap)
        #         heapq.heappush(rightheap, (costs[newrighti], newrighti))
        #         rightpoppedcount += 1
        #     else:
        #         if lefti < righti:
        #             totalCost += left
        #             # costs.remove(left)
        #             heapq.heappop(leftheap)
        #             heapq.heappush(leftheap, (costs[newlefti], newlefti))
        #             leftpoppedcount += 1
        #         else:
        #             totalCost += right
        #             # costs.remove(right)
        #             heapq.heappop(rightheap)
        #             heapq.heappush(rightheap, (costs[newrighti], newrighti))
        #             rightpoppedcount += 1


        # print(totalCost)
        # return totalCost
        i = 0 
        j = len(costs) - 1
        pq1 = []
        pq2 = []
        ans = 0
        while k > 0:
            while len(pq1) < candidates and i <= j:
                heapq.heappush(pq1, costs[i])
                i += 1
            while len(pq2) < candidates and i <= j:
                heapq.heappush(pq2, costs[j])
                j -= 1

            num1 = pq1[0] if pq1 else float("infinity")
            num2 = pq2[0] if pq2 else float("infinity")

            if num1 <= num2:
                ans += num1
                heapq.heappop(pq1)
            else:
                ans += num2
                heapq.heappop(pq2)

            k -= 1
        print(ans)
        return ans
sln = Solution()
sln.totalCost([17,12,10,2,7,2,11,20,8], 3, 4)
# sln.totalCost([1,2,4,1], 3, 4)