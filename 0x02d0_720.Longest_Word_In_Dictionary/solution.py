class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words = sorted(words)
        # print words

        d = {"": 1}
        longest = ""
        for word in words:
            if word[:-1] in d:
                d[word] = 1
                if len(word) > len(longest):
                    longest = word
        return longest
