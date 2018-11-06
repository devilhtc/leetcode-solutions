class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cs = []
        for c in s:
            if re.match(r'[a-zA-Z0-9]', c):
                cs.append(c.lower())
       
        for i in range(len(cs)):
            j = len(cs) - i - 1
            if j <= i:
                break
            elif cs[i] != cs[j]:
                return False
            
        return True
        