class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c1=0
        c2=0
        c0=0
        for i in nums:
            if i==0:
                c0+=1
            elif i==1:
                c1+=1
            elif i==2:
                c2+=2
        for i in range(c0):
            nums[i]=0
        for i in range(c0,c0 + c1):
            nums[i]=1
        for j in range(c0 + c1,len(nums)):
            nums[j]=2        

