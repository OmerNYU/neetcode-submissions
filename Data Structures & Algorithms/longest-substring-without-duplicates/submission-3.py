class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
            
        l, r = 0, 0

        seen = set()
        longest = 0
        length = r - l
        while r < len(s):

            if s[r] not in seen:
                seen.add(s[r])
                longest = max(longest, r - l + 1)
                r += 1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
        
        return longest
        