class Solution(object):
    def longestCommonPrefix(self, l):
        if l == []:
            return ''
        
        min_string = min([len(s) for s in l])
        result = ''
        
        for i in range(min_string):
            string = l[0][i]
            flag = 1
          
            for s in l:
                if string != s[i]:
                    flag = 0
                    break
                  
            if not(flag):
                break
            result += string
        return result
