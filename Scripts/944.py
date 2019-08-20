class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        # deleteIdx = []
        # ans = 0
        # for char_idx in range(len(A[0])):
        #     tmp = 0
        #     for word_idx in range(len(A)):
        #         if tmp > ord(A[word_idx][char_idx]):
        #             deleteIdx.append(char_idx)
        #             break
        #         tmp = ord(A[word_idx][char_idx])
        # return len(deleteIdx)
        
        A2 = zip(*A)
        ans = 0
        for string in A2:
            if string != tuple(sorted(string)):
                ans += 1
        
        return ans