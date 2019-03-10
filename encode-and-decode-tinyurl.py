class Codec:
    import string
    letters = string.ascii_letters + string.digits  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
    full_tiny = {}
    tiny_full = {}
    global_counter = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL. 

        :type longUrl: str 
        :rtype: str 
        """
        def decto62(dec):
            ans = ""
            while 1:
                ans = self.letters[dec % 62] + ans
                dec //= 62
                if not dec:
                    break
            return ans

        suffix = decto62(self.global_counter)
        if longUrl not in self.full_tiny:
            self.full_tiny[longUrl] = suffix
            self.tiny_full[suffix] = longUrl
            self.global_counter += 1
        return "http://tinyurl.com/" + suffix

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL. 

        :type shortUrl: str 
        :rtype: str 
        """
        idx = shortUrl.split('/')[-1]
        if idx in self.tiny_full:
            return self.tiny_full[idx]
        else:
            return None

longUrl ='https://leetcode.com/problems/design-tinyurl'
res1 = Codec().encode(longUrl)
res2 = Codec().decode(res1)
print(res1)
print(res2)
