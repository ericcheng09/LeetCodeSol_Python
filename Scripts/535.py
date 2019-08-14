import random
urlMap = {}
class Codec:
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in urlMap.values():
            for k, v in urlMap.items():
                if v == longUrl:
                    return k
        tinyUrlLen = random.randint(5,10)
        output = "http://tinyurl.com/"
        for i in range(tinyUrlLen):
            output += chr(random.randint(ord('A'),ord('Z')))
        urlMap[output] = longUrl
        return output
        
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return urlMap[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))