class Solution:
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1   
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        if n==1:
            return
        i=n-2
        #finding the pivot element i
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1    
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            self.reverse(nums, i + 1, n - 1)
        else:
            self.reverse(nums, 0, n - 1)
