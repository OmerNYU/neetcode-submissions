class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        final_k = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        sorted_by_value = sorted(count.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            final_k.append(sorted_by_value[i][0])

        return final_k
        