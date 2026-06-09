class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 1
        for i_idx, i in enumerate(nums): 
            solution = target - i
            if solution in nums[index:]:
                return [i_idx, nums.index(solution, index)]
            else:
                index += 1
