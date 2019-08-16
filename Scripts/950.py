class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        idxs = range(len(deck)) # the index of answer
        deck.sort()
        ans = [0] * len(deck)
        draw = True
        while(True):
            if not idxs: 
                break
            if draw:
                draw = False
                ans[idxs.pop(0)] = deck.pop(0)
                # put the smallest card in deck to the index of answer
            else:
                idxs = idxs[1:] + [idxs[0]]
                # put the current idx to the end of list (bottom of deck)
                draw = True
        
        return ans