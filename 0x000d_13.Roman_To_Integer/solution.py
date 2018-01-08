ROMAN1 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
ROMAN2 = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
ROMAN3 = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        if s.startswith('M'):
            return 1000 + self.romanToInt(s[1:])
        romanlists = [ROMAN3, ROMAN2, ROMAN1]
        for i in range(3):
            for j in range(9, 0, -1):
                if s.startswith(romanlists[i][j]):
                    return j * (10 ** (2 - i)) + self.romanToInt(s[len(romanlists[i][j]):])
        return 0
        
        