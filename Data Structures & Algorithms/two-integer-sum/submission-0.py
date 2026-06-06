class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_tracker=dict()

        for i,n in enumerate(nums):
            diff=target-n

            if diff in sum_tracker.keys():
                return[sum_tracker[diff],i]
            
            sum_tracker[n]=i
