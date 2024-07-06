from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        def isOverlap(interval, num):
            return interval[0] <= num <= interval[1]
        newIntervals = []
        mergeStartIndex, mergeEndIndex = -2, -2
        for i, interval in enumerate(intervals):
            if mergeStartIndex == -2 and (isOverlap(interval, newInterval[0]) or isOverlap(newInterval, interval[0])):
                mergeStartIndex = i
            elif (isOverlap(interval, newInterval[1]) or isOverlap(newInterval, interval[1])):
                mergeEndIndex = i

        if mergeStartIndex != -2 and mergeEndIndex == -2:
            mergeEndIndex = mergeStartIndex
        elif mergeStartIndex == -2 and mergeEndIndex != -2:
            mergeStartIndex = mergeEndIndex

        if mergeStartIndex == -2 and mergeEndIndex == -2:
            appended = False
            for i, interval in enumerate(intervals):
                if newInterval[1] < interval[0] and not appended:
                    newIntervals.append(newInterval)
                    appended = True
                    
                newIntervals.append(interval)

            if not appended:
                newIntervals.append(newInterval)
        else:
            for i in range(0, mergeStartIndex):
                newIntervals.append(intervals[i])

            minVal = min(intervals[mergeStartIndex][0], newInterval[0])
            maxVal = max(intervals[mergeEndIndex][1], newInterval[1])
            combinedInterval = [minVal, maxVal]
            newIntervals.append(combinedInterval)

            for i in range(mergeEndIndex + 1, len(intervals)):
                newIntervals.append(intervals[i])

        print(newIntervals)
        return newIntervals
    
sln = Solution()
# ans = sln.insert([[1,3],[6,9]], [2,5])
# ans = sln.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
# ans = sln.insert([], [4,8])
# ans = sln.insert([[1,5]], [0,6])
ans = sln.insert([[2,5],[6,7]], [8,9])
ans = sln.insert([[2,5],[6,7],[12,13], [14,15]], [0,1])
# print(ans)