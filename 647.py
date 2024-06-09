class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        - Sliding window
        - substrings
        - Left move condition - not palindrome

        '''
        n, palindromes = len(s), 0
        for i in range(n):
            odd = self.palindromeCount(i, i, s)
            even = self.palindromeCount(i, i+1, s)
            palindromes += odd + even
        return palindromes
    
    def palindromeCount(self, left, right, s):
        count = 0
        n = len(s)
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1
        return count
    
sln = Solution()
# ans = sln.countSubstrings("aaa") # 3
ans = sln.countSubstrings("fsdlkf") # 3

print(ans)