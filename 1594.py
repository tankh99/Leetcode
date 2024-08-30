from typing import List

# # Kruskal's Algorithm
# class UnionFind:
#     def __init__(self, n):
#         self.parent = list(range(n))  # Each element is its own parent
#         self.rank = [1] * n           # Rank (or size) of each set is 1

#     def find(self, u):
#         if self.parent[u] != u:
#             self.parent[u] = self.find(self.parent[u])  # Path compression
#         return self.parent[u]

#     def union(self, u, v):
#         root_u = self.find(u)
#         root_v = self.find(v)

#         if root_u != root_v:
#             # Union by rank
#             if self.rank[root_u] > self.rank[root_v]:
#                 self.parent[root_v] = root_u
#             elif self.rank[root_u] < self.rank[root_v]:
#                 self.parent[root_u] = root_v
#             else:
#                 self.parent[root_v] = root_u
#                 self.rank[root_u] += 1

#     def is_same_set(self, u, v):
#         return self.find(u) == self.find(v)

# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         n, m = len(points), len(points[0])
#         ufds = UnionFind(n * m)

#         # Use the values!
#         def manhattan_dist(point1, point2):
#             r1,c1 = point1
#             r2,c2 = point2
#             return abs(r2-r1) + abs(c2-c1)
        
#         edges = []
        
#         for i in range(n):
#             point1 = points[i]
#             for j in range(i+1, n):
#                 point2 = points[j]
#                 if i == j: continue
#                 edges.append((i, j, abs(manhattan_dist(point1, point2))))
        

#         edges = sorted(edges, key=lambda x: x[2])
#         print(edges)
#         mst_sum = 0
#         for edge in edges:
#             a, b, dist = edge
#             if ufds.is_same_set(a,b):
#                 continue
#             ufds.union(a,b)
#             mst_sum += dist
#         # print(mst_sum)
#         return mst_sum

from heapq import heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, m = len(points), len(points[0])

        # Use the values!
        def manhattan_dist(point1, point2):
            r1,c1 = point1
            r2,c2 = point2
            return abs(r2-r1) + abs(c2-c1)
        
        # al = []
        
        # for i in range(n):
        #     point1 = points[i]
        #     sub_al = []
        #     for j in range(n):
        #         point2 = points[j]
        #         if i == j: continue
        #         sub_al.append((abs(manhattan_dist(point1, point2)), i, j))
        #     al.append(sub_al)
        
        pq = []
        heappush(pq, (0, 0, 0))
        seen = [False for _ in range(n)]
        mst_sum = 0
        # print(al)
        while pq:
            weight, a, b = heappop(pq)
            if seen[b]:
                continue
            seen[b] = True
            # print(weight,a,b)
            mst_sum += weight
            for j in range(n):
                neighbour = points[j]
                if j == b: continue
                if not seen[j]:
                    point1 = points[b]
                    # ] = neighbour
                    # print(point1, neighbour)

                    heappush(pq, (abs(manhattan_dist(point1, neighbour)), b,j))
        return mst_sum
sln = Solution()
# ans = sln.minCostConnectPoints([[3,12],[-2,5],[-4,1]])
# ans = sln.minCostConnectPoints([[0,0],[1,1],[1,0],[-1,1]])
ans = sln.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])
print(ans)

# sln.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])