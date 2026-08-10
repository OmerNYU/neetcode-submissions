class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        freq_count = defaultdict(int)
        max_freq = 0
        max_window = 0


        for r in range(len(s)):
            window_size = r - l + 1
            freq_count[s[r]] += 1
            max_freq = max(max_freq, freq_count[s[r]])
            while (window_size - max_freq > k):
                freq_count[s[l]] -= 1
                l += 1
                window_size = r - l + 1
            max_window = max(max_window, window_size)
            


        return max_window
