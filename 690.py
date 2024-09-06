from collections import deque
from heapq import heappop, heappush
from typing import List


class Solution:
  # A A A B B B
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = []
        freq_map = {}
        curr_time = 0
        for task in tasks:
            if task not in freq_map:
                freq_map[task] = 0
            freq_map[task] += 1
        cooldown_queue = deque()

        for task, freq in freq_map.items():
            heappush(pq, (-freq, task))
        
        while pq or cooldown_queue:

            if pq:
                freq, task = heappop(pq)
                if freq + 1 < 0:
                    cooldown_queue.append((task, curr_time + n, freq + 1))
                    # heappush(pq, (freq + 1, task))

            if cooldown_queue and cooldown_queue[0][1] == curr_time:
                last_task, last_time, last_freq = cooldown_queue.popleft()
                heappush(pq, (last_freq, last_task))

            curr_time += 1
        return curr_time
    
sln = Solution()
arr = ["A","A","A","B","B","B"]

ans = sln.leastInterval(arr, 2)
print(ans)
