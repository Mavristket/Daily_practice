class Solution:
    def reverseWords(self, s):
        parts=s.split(".")
        words = [word for word in parts if word != ""]
        words.reverse()
        return ".".join(words)
        