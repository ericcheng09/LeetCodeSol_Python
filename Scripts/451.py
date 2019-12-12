class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        record = {}
        max_len = 0
        for c in s:
            record[c] = record.get(c, 0) + 1
            if record[c] > max_len:
                max_len = record[c]
                
        tmp = [""] * max_len
        for key, val in record.items():
            tmp[val - 1] += key * val
        return "".join(tmp[::-1])