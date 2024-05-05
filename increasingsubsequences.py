from typing import List

def increasingTriplet(nums: List[int]) -> bool:
    a = b = float('inf')

    for num in nums:
        if num <= a:
            a = num
        elif num > a and num <= b:
            b = num
        elif num > a and num > b:
            return True
        
    return False

isIncreasing = increasingTriplet([10, 9, 3, 4, 0, 5])
print(isIncreasing)

def testIncreasingTriplets(nums):
    lowest = nums[0]
    count = 0
    for i in range(1, len(nums)):
        if nums[i] < lowest:
            lowest = nums[i]
        elif nums[i] > lowest:
            count += 1
    return count >= 3

# testIncreasingTriplets([8, 1,5,4,5,6])