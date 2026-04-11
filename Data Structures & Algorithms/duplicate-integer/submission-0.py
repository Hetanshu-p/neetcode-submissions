class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appear_list = []
        for i in nums: 
            if i in appear_list: 
                return True
            else: 
                appear_list.append(i)
        return False