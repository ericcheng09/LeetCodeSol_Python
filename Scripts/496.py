class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = [-1] * len(nums1)
        for idx, num in enumerate(nums1):
            idxNum2 = nums2.index(num) + 1
            while idxNum2 < len(nums2):
                if nums2[idxNum2] > num:
                    ans[idx] = nums2[idxNum2]
                    break
                idxNum2 += 1
        return ans
                