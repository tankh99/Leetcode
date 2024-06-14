from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        
        for word in strs:
            sortedWord = ''.join(sorted(word))
            dict[sortedWord].append(word)
        return [dict[key] for key in dict]
    
sln = Solution()
# ans = sln.groupAnagrams(["abc", "bca", "acb"]) # [["bat"],["nat","tan"],["ate","eat","tea"]]
ans = sln.groupAnagrams(["ddddddddddg","dgggggggggg"]) # [["bat"],["nat","tan"],["ate","eat","tea"]]
# ans = sln.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) # [["bat"],["nat","tan"],["ate","eat","tea"]]

# ans = sln.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(ans)

# def isAnagram(s1, s2):
#     map = {}
#     map["a"] = 0
#     map["b"] = 1
#     for key in map:
#         print(key)
        
# isAnagram("abc", "bca")