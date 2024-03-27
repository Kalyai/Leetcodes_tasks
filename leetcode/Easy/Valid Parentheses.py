class Solution(object):
    def isValid(self, s):
        def check(function):
            if len(stack) > 0 and stack[-1] == function:
                stack.pop()
                return True
            return False

        stack = list()
        for s1 in s:
            if s1 in '([{':
                stack.append(s1)

            elif s1 == ')':
                if not (check('(')):
                    return False

            elif s1 == ']':
                if not (check('[')):
                        return False

            elif s1 == '}':
                if not(check('{')):
                    return False
                
        if len(stack) == 0:
            return True
        return False
        
