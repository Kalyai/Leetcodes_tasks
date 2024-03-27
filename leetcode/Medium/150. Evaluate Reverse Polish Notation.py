class Solution(object):
    def evalRPN(self, tokens):
        def check(operation):
            def clear_stack(value):
                stack.pop()
                stack.pop()
                stack.append(value)

            if operation == '+':
                value = stack[-2] + stack[-1]
                clear_stack(value)

            elif operation == '-':
                value = stack[-2] - stack[-1]
                clear_stack(value)

            elif operation == '*':
                value = stack[-2] * stack[-1]
                clear_stack(value)

            else:
                value = int(float(stack[-2]) / float(stack[-1]))
                clear_stack(value)

        stack = list()
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                check(token)
        return stack[-1]
