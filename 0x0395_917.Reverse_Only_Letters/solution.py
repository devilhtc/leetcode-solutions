class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        a, z, A, Z = ord('a'), ord('z'), ord('A'), ord('Z')
        def isletter(c):
            return (a <= ord(c) <= z) or (A <= ord(c) <= Z)
        buffer = list(S)
        i = 0
        j = len(S) - 1
        while j > i:
            while i < len(S) and not isletter(buffer[i]):
                i += 1
            while j >= 0 and not isletter(buffer[j]):
                j -= 1
            if j > i and i < len(S) and j >= 0:
                buffer[i], buffer[j] = buffer[j], buffer[i]
                i += 1
                j -= 1
        return ''.join(buffer)
            