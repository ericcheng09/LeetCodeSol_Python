class Solution:
    def judgeCircle(self, moves):
        pos = [0,0]
        for char in moves:
            if char == 'U':
                pos[1] += 1
            if char == 'D':
                pos[1] -= 1
            if char == 'R':
                pos[0] += 1
            if char == 'L':
                pos[0] -= 1
        if pos[0] == 0 and pos[1] == 0:
            return True
        else:
            return False
            
        """
        :type moves: str
        :rtype: bool
        """
        