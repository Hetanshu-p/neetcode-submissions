class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        solution = []
        nums.sort()
        print(nums)
        tempSol = [nums[0]]
        for i in range(1, len(nums)): 
            if nums[i] - nums[i-1] == 1 or nums[i] - nums[i-1] == -1:
                tempSol.append(nums[i])
            elif nums[i] - nums[i-1] == 0:
                continue
            else: 
                if len(tempSol) > len(solution):
                    solution = tempSol
                    tempSol = [nums[i]]
                else: 
                    tempSol = [nums[i]]
        if len(tempSol) > len(solution):
            return len(tempSol)
        else: 
            return len(solution)