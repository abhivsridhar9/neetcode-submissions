class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Initial solution with sorting
        # sorted_nums=sorted(nums)
        # if len(sorted_nums)>0 and sorted_nums[0]!=0:
        #     return 0
        
        # for i in range(len(sorted_nums)-1):
        #     if sorted_nums[i+1]-sorted_nums[i]>1:
        #         return sorted_nums[i]+1
        
        # return sorted_nums[len(sorted_nums)-1]+1

        # With sum formula
        l=len(nums)
        s=(l*(l+1))//2

        for i in nums:
            s-=i
        
        return s
