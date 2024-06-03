from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions.sort()
        for spell in spells:
            low = 0
            high = len(potions) - 1
            # Determine the minimum index to satisfy success criteria
            best_potion_idx = float('inf')
            while low <= high:
                mid = (low + high) // 2
                result = potions[mid] * spell
                # Reduce high so that we get the minimum mid index
                if result >= success:
                    high = mid - 1
                    # The smaller the potion index, the better the result it is
                    if best_potion_idx > mid:
                        best_potion_idx = mid
                else:
                    # increase low so that we can find the minimum mid index
                    low = mid + 1
            # use the minimum index (mid) to find the nubmer of possible pairs

            numPairs = len(potions) - best_potion_idx if (best_potion_idx != float("inf")) else 0

            pairs.append(numPairs)
            # find the minimum potion strength that meets success criteria
        return pairs
        
sln = Solution()

ans = sln.successfulPairs([5,1,3], [1, 2, 3, 4,5], 7)
print(ans)
