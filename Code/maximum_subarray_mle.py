class Solution:
    def generateSubarrays(self,arr):
        subarr=[]
        n=len(arr)
        for i in range(n):
            arry=[]
            for j in range(i,n):
                arry.append(arr[j]) 
                subarr.append(arry.copy())
        return subarr         
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        else:    
            subarr=self.generateSubarrays(nums)
            print(subarr)
            sum_arr=[]
            for i in subarr:
                sum_arr.append(sum(i))
            return max(sum_arr)    