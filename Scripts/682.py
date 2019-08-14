class Solution:
    def calPoints(self, ops):
        valid_score = list()
        for i in range(len(ops)):
            if ops[i] == 'C':
                valid_score.pop()
            elif ops[i] == 'D':
                last_valid_score = valid_score.pop()
                valid_score.append(last_valid_score)
                valid_score.append(last_valid_score * 2)
            elif ops[i] == '+':
                t1 = valid_score.pop()
                t2 = valid_score.pop()
                valid_score.append(t2)
                valid_score.append(t1)
                valid_score.append(t1 + t2)
            else:
                valid_score.append(int(ops[i]))
        return sum(valid_score)
        
       