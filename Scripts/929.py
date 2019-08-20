class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniqueAddress = set()
        for email in emails:
            emailParts = email.split("@")
            actualAddress = (emailParts[0].split("+"))[0].replace(".","") + "@" + emailParts[1]
            uniqueAddress.add(actualAddress)
            
        return len(uniqueAddress)