class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest_sub = 0

        seen = set()

        while r < len(s):
            curr_length = r - l 
            if s[r] not in seen:
                curr_length += 1
                longest_sub = max(longest_sub, curr_length)
                seen.add(s[r])
                r += 1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1

            

        return longest_sub
