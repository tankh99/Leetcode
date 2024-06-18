from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = {}
        edges = {}
        for course in range(numCourses):
            indeg[course] = 0
            edges[course] = []
        
        for prereq in prerequisites:
            fromCourse, toCourse = prereq
            indeg[toCourse] += 1
            
            edges[fromCourse].append(toCourse)

        q = deque()

        for course in indeg:
            if indeg[course] == 0:
                q.append(course)
        
        coursesSeen = 0

        while q:
            curr = q.popleft()
            currEdges = edges[curr]
            coursesSeen += 1
            for i, to in enumerate(currEdges):
                indeg[to] -= 1
                if indeg[to] == 0:
                    q.append(to)

        
        return coursesSeen == numCourses
  
sln = Solution()
# sln.canFinish(2, [[0,1]])
sln.canFinish(2, [[0,1], [1,0]])
# sln.canFinish(5, [[0,1], [0,2], [1,3], [2,4], [3,2]])
# sln.canFinish(6, [[0,1], [0,2], [1,3], [2,4], [3,2]])