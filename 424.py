from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, max_count, max_length = 0, 0, 0
        counter = Counter()
        for r, c in enumerate(s):
            counter[c] += 1
            max_count = max(max_count, counter[c])
            if r - l + 1 - max_count > k:
                counter[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)
        return max_length
sln = Solution()
ans = sln.characterReplacement("ABAB", 2)
print(ans)
# ans = sln.characterReplacement("ABBAAAAAABAB", 2)