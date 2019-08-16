class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lastOcur = {}
        
        for index ,s in enumerate(S):
            lastOcur[s] = index
        ans = []
        lastIdxofPartition = 0
        partition_startIdx = 0
        for index ,s in enumerate(S):
            if lastOcur[s] > lastIdxofPartition:
                # the partition will be extended
                # because  letter 's' existed in this partition
                # but it has bigger index than the index of end of partition
                lastIdxofPartition = lastOcur[s]
            if index == lastIdxofPartition: # this partition ends
                ans.append(1 + lastIdxofPartition - partition_startIdx)
                partition_startIdx = index + 1 # set new start index to partition
        return ans