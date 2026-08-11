class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_count = defaultdict(int)
        for char in t:
            t_count[char] += 1
        
        need = len(t_count)

        l, r, have = 0,0,0
        best_start = 0
        best_len = float("inf")

        curr_window = defaultdict(int)

        while r < len(s):
            if s[r] in t_count:
                curr_window[s[r]] += 1
                if curr_window[s[r]] == t_count[s[r]]:
                    have += 1
            r += 1
            while have == need:
                current_len = r - l
                if current_len < best_len:
                    best_len = current_len
                    best_start = l
                curr_window[s[l]] -= 1
                if s[l] in t_count and curr_window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        if best_len == float("inf"):
            return ""
            
        return s[best_start:best_start + best_len]

