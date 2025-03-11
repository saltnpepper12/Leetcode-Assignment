class Solution:
    def reverseWords(self, s):
        s = s[::-1]
        w = []
        i = 0
        n = len(s)
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            start = i
            while i < n and s[i] != ' ':
                i += 1
            if start < i:
                w.append(s[start:i][::-1])
        return " ".join(w)