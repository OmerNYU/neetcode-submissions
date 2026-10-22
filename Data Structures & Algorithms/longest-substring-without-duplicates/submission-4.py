class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0

        seen = set()
        max_len = 0

        if len(s) == 0:
            return 0

        curr_len = 0
        while l <= r and r < len(s):

            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1
                curr_len = r - l
                max_len = max(curr_len, max_len)
            
            while r < len(s) and s[r] in seen:
                seen.remove(s[l])
                l += 1
                

            
        return max_len
            

