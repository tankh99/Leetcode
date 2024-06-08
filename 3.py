from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, max_l = 0, 0
        seen = Counter()
        for r, c in enumerate(s):
            if seen[c] and seen[c] > 0:
                while True:
                    seen[s[l]] -= 1
                    if seen[s[l]] == 0:
                        del seen[s[l]]
                    l += 1
                    if seen[c] == 0:
                        break
            seen[c] += 1

            max_l = max(max_l, len(seen))
        return max_l

sln = Solution()
ans = sln.lengthOfLongestSubstring("aabaab!bb")
print(ans)
ans = sln.lengthOfLongestSubstring("abcabcabc")
print(ans)
ans = sln.lengthOfLongestSubstring("bbbbb")
print(ans)
ans = sln.lengthOfLongestSubstring("pwwkew")
print(ans)
ans = sln.lengthOfLongestSubstring("jbpnbwwd")
print(ans)
ans = sln.lengthOfLongestSubstring("qrsvbspk")
print(ans)