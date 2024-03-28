class Solution(object):
    def backspaceCompare(self, s, t):
        new_s, new_t = '', ''

        i = 0
        while i != len(s):
            if s[i] == '#':
                new_s = new_s[:-1]
            else:
                new_s += s[i]
            i += 1

        i = 0
        while i != len(t):
            if t[i] == '#':
                new_t = new_t[:-1]
            else:
                new_t += t[i]
            i += 1

        return new_s == new_t
