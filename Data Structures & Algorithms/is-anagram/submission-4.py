class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = defaultdict(int)

        for char in s:
            seen[char] += 1
        
        for char in t:
            if char not in seen or seen[char] < 0:
                return False
            else:
                seen[char] -= 1
        
        return all(value == 0 for value in seen.values())



        