MORSE_DICT = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

def encode(w):
    out_list = []
    for c in w:
        out_list.append(MORSE_DICT[ord(c) - ord('a')])
    return ''.join(out_list)

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        s = set([])
        for w in words:
            s.add(encode(w))
        return len(s)
        