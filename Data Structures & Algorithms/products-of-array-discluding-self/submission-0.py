class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        res = []
        
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                product *= num
        
        for num in nums:
            if zeros > 1:
                res.append(0)
            elif zeros == 1:
                if num == 0:
                    res.append(product)
                else:
                    res.append(0)
            else:
                res.append(product // num)
        return res