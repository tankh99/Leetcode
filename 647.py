class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        - Sliding window
        - substrings
        - Left move condition - not palindrome

        '''
        palindromes = 0
        for i in range(len(s)):
            curr = ""
            for j in range(i, len(s)):
                curr += s[j]
                if self.isPalindrome(curr):
                    palindromes += 1

        return palindromes

    def isPalindrome(self, s):
        mid = len(s) // 2
        if len(s) % 2 != 0:
            firstHalf = s[:mid]
            reversedSecondHalf = s[mid+1:][::-1]
        else:
            firstHalf = s[:mid]
            reversedSecondHalf = s[mid:][::-1]
        return firstHalf == reversedSecondHalf
    
sln = Solution()
# ans = sln.countSubstrings("aaa") # 3
ans = sln.countSubstrings("fsdlkf") # 3

print(ans)