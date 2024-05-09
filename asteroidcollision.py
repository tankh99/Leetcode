# https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def sameSign(self, a, b):
        return a * b >= 0
    
    # REtursn the victor depending on the size of the asteroids. 
    # -1 = left wins, 0 = both die, 1 = right wins, 2 = no collision
    def checkCollision(self, top, curr):
        top_dir = 1 if top > 0 else -1
        curr_dir = 1 if curr > 0 else -1
        if top_dir == curr_dir or (top_dir == -1 and curr_dir == 1):
            return 2
        
        else:
            # Means that top is right and curr is left. COLLISION INBOUND
            # Check for size tosee if top breaks or curr breaks first
            
            if abs(top) > abs(curr):
                return -1
            elif abs(top) == abs(curr):
                return 0
            else:
                return 1


    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            if len(stack) > 0:
                top = stack[-1]
                collisionResult = self.checkCollision(top, num)
                if collisionResult == 2:
                    stack.append(num)
                else:
                    still_alive = True
                    while len(stack) > 0:
                        top = stack[-1]
                        collisionResult = self.checkCollision(top, num)
                        if collisionResult == -1:
                            still_alive = False
                            break
                        elif collisionResult == 0:
                            stack.pop()
                            still_alive = False
                            break
                        elif collisionResult == 1:
                            stack.pop()
                        else:
                            print("Uh oh")
                            break
                    # HANDLE CASE WHERE RIGHT ASTEROID DESTORYS EVERYTHING
                    if still_alive:
                        stack.append(num)
                    # if len(stack) == 0:
                    #     stack.append()
            else:
                stack.append(num)

        print(stack)
        return stack
    
sln = Solution()
sln.asteroidCollision([-2, -2, 1, -2])
# sln.asteroidCollision([8, -8])
# sln.asteroidCollision([5,4,3,-10])