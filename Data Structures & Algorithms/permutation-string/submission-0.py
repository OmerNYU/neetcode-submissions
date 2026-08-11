class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l, r = 0, len(s1) 
        
        s1_window = defaultdict(int)
        curr_window = defaultdict(int)

        for i in range(len(s1)):
            s1_window[s1[i]] += 1

        for i in range(l, r):
            curr_window[s2[i]] += 1
            
        while r < len(s2):

            if s1_window == curr_window:
                return True
            else:
                curr_window[s2[l]] -= 1
                if curr_window[s2[l]] == 0:
                    del curr_window[s2[l]]
                l += 1
                
                curr_window[s2[r]] += 1
                r += 1
        return s1_window == curr_window
        
        