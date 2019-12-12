class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # we conut the number of lists that complement each other
        # EX: [1, 0, 0]. [0, 1, 1] we consider them as same pattern
        # we count the "pattern" and return max count of pattern
        count_dict = {}
        for row in matrix:
            if row[0] == 1:
                key = ''.join(map(str, [0 if n == 1 else 1 for n in row]))
            else:
                key = ''.join(map(str, row))
            count_dict[key] = count_dict.get(key, 0) + 1

        return max(count_dict.values())
