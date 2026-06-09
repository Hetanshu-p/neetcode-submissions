class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        dict1 = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
        solution = list(dict1.keys())[:k]
        return solution