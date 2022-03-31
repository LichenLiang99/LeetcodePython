class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        product = 1
        l = 0
        res = 0
        
        for r, n in enumerate(nums):
            product *= n
            while product >= k:
                product /= nums[l]
                l += 1
            
            res += r - l + 1
        
        return res