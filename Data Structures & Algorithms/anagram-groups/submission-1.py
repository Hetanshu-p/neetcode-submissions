class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = []
        seen = set()
        for i in range(len(strs)):
            if i in seen:
                continue
            sorted_i = "".join(sorted(strs[i]))
            sorted_i_list = [strs[i]]
            for j in range(i+1, len(strs)): 
                sorted_j = "".join(sorted(strs[j]))
                if sorted_i == sorted_j:
                    seen.add(j)
                    sorted_i_list.append(strs[j])
            solution.append(sorted_i_list)
        return solution


                
            


        