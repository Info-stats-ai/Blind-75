class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
    
        def dfs(current, current_sum, total_sum):
            if current_sum == target:
                res.append(total_sum.copy())
                return
            if current_sum > target or current >= len(candidates):
                return
            
            total_sum.append(candidates[current])
            dfs(current, current_sum + candidates[current], total_sum)
            total_sum.pop()
            
            dfs(current + 1, current_sum, total_sum)
        
        dfs(0, 0, [])
        return res
        