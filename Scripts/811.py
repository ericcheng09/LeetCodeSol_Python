class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
        countNamePairs = {}
        tmp = {}
        for s in cpdomains:
            parts = s.split(" ")
            times = int(parts[0])
            subs = parts[1].split(".")[::-1]
            domains = []
            sub = ""
            for idx, s in enumerate(subs):
                sub = s + sub
                if countNamePairs.get(sub):
                    countNamePairs[sub] += times
                else:
                    countNamePairs[sub] = times
                sub = "." + sub
                
                

                
        return [ str(times) + " " + sub for sub, times in countNamePairs.items()]
        
    