from collections import Counter
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s1, s2):
            map1 = Counter(s1)
            map2 = Counter(s2)
            return map1 == map2
        
        n = len(strs)
        
        if n == 0:
            return [[""]]
        
        ans = []
        seen = set()

        '''
        1. Lock the first number
        2. Nested for loop the rest of the nubmers in the list 
        3. In each iteration, append a new array. Then check if word1 and word2 is anagram. If so, then add them to the current array
        
        '''
        for i in range(n):
            word1 = strs[i]
            # We skip word because it has already been added to an anagram group
            if word1 in seen:
                continue
            seen.add(word1)
            ans.append([word1])

            for j in range(i+1, n):
                word2 = strs[j]
                same = isAnagram(word1, word2)
                    
                if same:
                    seen.add(word2)
                    ans[-1].append(word2)
                
        return ans
    
sln = Solution()
# ans = sln.groupAnagrams(["abc", "bca", "acb"]) # [["bat"],["nat","tan"],["ate","eat","tea"]]
ans = sln.groupAnagrams(["ddddddddddg","dgggggggggg"]) # [["bat"],["nat","tan"],["ate","eat","tea"]]
# ans = sln.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) # [["bat"],["nat","tan"],["ate","eat","tea"]]

# ans = sln.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(ans)

def isAnagram(s1, s2):
    map = Counter(s1)
    map2 = Counter(s2)
    print(map, map2, map == map2)
        
isAnagram("abc", "bca")