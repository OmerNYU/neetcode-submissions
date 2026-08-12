class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', '}': '{', ']': '['}
        opening = {'(' ,'{', '['}
        stack = deque()

        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if stack and match[char] == stack[-1]:
                        stack.pop()
                else:
                    return False
        
        return not stack