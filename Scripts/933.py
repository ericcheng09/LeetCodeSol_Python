class RecentCounter(object):

    def __init__(self):
        self.pingsRecent = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        
        self.pingsRecent.append(t)
        while True:
            if self.pingsRecent[0] < t - 3000:
                self.pingsRecent.pop(0)
            else:
                break
        return len(self.pingsRecent)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)