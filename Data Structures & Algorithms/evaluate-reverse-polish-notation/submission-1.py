class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                if token == "+":
                    a = stack.pop()
                    b = stack.pop()
                    res = a + b
                    stack.append(res)
    
                elif token == "-":
                    a = stack.pop()
                    b = stack.pop()
                    res = b - a
                    stack.append(res)
            
                elif token == "*":
                    a = stack.pop()
                    b = stack.pop()
                    res = a * b  
                    stack.append(res)                  

                else:  
                    a = stack.pop()
                    b = stack.pop()
                    res = int(b / a)
                    stack.append(res)
        res = stack.pop()

        return res
                

        