class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # return sorted(nums)
    
        # return self.bubbleSort(nums)
        self.mergeSort(nums)
        return nums
    
    def bubbleSort(self, nums):
        # take too much time
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j+1]:
                    # swap
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
    
    def selectionSort(self, nums):
        for i in range(len(nums)):
            minN = min(nums[i:])
            idx = nums[i:].index(minN)
            nums[i+idx] = nums[i]
            nums[i] = minN
        return nums
    
    # assume left part of list is sorted, insert the new element to right place in left part
    def insertionSort(self, nums): 
        
        for i in range(1, len(nums)):
            idx = i - 1
            numToSort = nums[i]
            while idx >= 0 and numToSort < nums[idx]:
                nums[idx+1] = nums[idx] # move to right
                idx -= 1
            nums[idx+1] =  numToSort
    
    def mergeSort(self, nums):
        if len(nums) > 1: 
            middle = len(nums)//2
            left = nums[:middle] 
            right = nums[middle:] 

            self.mergeSort(left)
            self.mergeSort(right)
            
            
            mergeIdx = 0
            leftIdx = 0
            rightIdx = 0
            while leftIdx < len(left) and rightIdx < len(right):
                if left[leftIdx] < right[rightIdx]:
                    nums[mergeIdx] = left[leftIdx]
                    leftIdx += 1
                else:
                    nums[mergeIdx] = right[rightIdx]
                    rightIdx += 1
                mergeIdx += 1
                
            while leftIdx < len(left):
                nums[mergeIdx] = left[leftIdx]
                leftIdx += 1
                mergeIdx += 1
            
            while rightIdx < len(right):
                nums[mergeIdx] = right[rightIdx]
                rightIdx += 1
                mergeIdx += 1
   
          
          