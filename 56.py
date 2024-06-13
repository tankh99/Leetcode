from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def withinInterval(num, interval):
            return interval[0] <= num <= interval[1]
        
        def isOverlapping(interval1, interval2):
            a1, a2 = interval1
            b1, b2 = interval2
            ''' overlapping cases 
            1. Left side is within interval
            2. Right side is within interval
            3. Both sides within interval
            4. Both sides outside interval
            '''
            # Cases 1, 2 and 3
            if withinInterval(a1, interval2) or withinInterval(a2, interval2):
                return True
            elif a1 <= b1 and a2 >= b2:
                return True
            return False
        
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        uniqueIntervals = [intervals[0]] 
        for i in range(1, n):
            currInterval = intervals[i]
            m = len(uniqueIntervals) # fix the length
            isUnique = True
            if isOverlapping(currInterval, uniqueIntervals[-1]):
                newLeft = min(currInterval[0], uniqueIntervals[-1][0])
                newRight = max(currInterval[1], uniqueIntervals[-1][1])
                uniqueIntervals[-1] = [newLeft, newRight]
                isUnique = False
            # for j in range(m):
            #     intervalToCompare = uniqueIntervals[j]
            #     if isOverlapping(currInterval, intervalToCompare):
            #         newLeft = min(currInterval[0], intervalToCompare[0])
            #         newRight = max(currInterval[1], intervalToCompare[1])
            #         uniqueIntervals[j] = [newLeft, newRight]
            #         isUnique = False
            if isUnique:
                uniqueIntervals.append(currInterval)
        return uniqueIntervals
    
sln = Solution()
ans = sln.merge([[1,3],[2,6],[8,10],[15,18]])
# ans = sln.merge([[1,3],[4,6],[2,5]])
print(ans)

