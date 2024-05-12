class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0
        
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum


# class Solution:  
#     def maxSubArray(self, nums: List[int]) -> int:
#         if len(nums)==1:
#             return nums[0]
#         else:    
#             subarrsum=float('-inf')
#             n=len(nums)
#             for i in range(n):
#                 curr_sum=0
#                 for j in range(i,n):
#                     curr_sum+=nums[j]
#                     subarrsum=max(curr_sum,subarrsum)
#             return subarrsum



                    
        # for num in nums:
        #     current_sum = max(num, current_sum + num)
        #     max_sum = max(max_sum, current_sum)