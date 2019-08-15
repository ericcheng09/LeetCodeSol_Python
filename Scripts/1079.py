class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        # using builtin library
        count = 0
        for i in range(1,len(tiles)+1):
            count += len(set(itertools.permutations(tiles, i)))
        return count
            