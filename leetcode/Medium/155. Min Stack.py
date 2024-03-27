class MinStack(object):
    def __init__(self):
        self.stack = []
        self.mi = []

    def push(self, val):
        self.stack.append(val)
        if self.mi and self.mi[-1] < val:
            return
        self.mi.append(val)

    def pop(self):
        if self.stack[-1] == self.mi[-1]:
            self.mi.pop()
            self.stack.pop()
        else:
            self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.mi[-1]
