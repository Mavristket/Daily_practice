class Solution:
    def reverseWords(self, s):
        parts=s.split(".")
        l=[]
        words = [word for word in parts if word != ""]
        words.reverse()
        return ".".join(words)
        