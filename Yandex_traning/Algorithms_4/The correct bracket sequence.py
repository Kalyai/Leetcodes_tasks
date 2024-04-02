a = str(input())
o = ['(', '[', '{']
c = [')', ']', '}']
stack = list()
res = ''
for i in a:
    if i in o:
        stack.append(i)
    if i in c:
        if len(stack) == 0:
            res = 'no'
            break
        else:
            if i == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    res = 'no'
                    break
            elif i == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    res = 'no'
                    break
            else:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    res = 'no'
                    break
if len(stack) == 0 and res != 'no':
    res = 'yes'
else:
    res = 'no'
print(res)
