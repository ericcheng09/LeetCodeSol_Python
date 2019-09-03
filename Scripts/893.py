class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        permutations = set()
        for word in A:
            tmp = "".join(sorted(word[::2]) + sorted(word[1::2]))

            permutations.add(tmp)
        return len(permutations)