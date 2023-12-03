class NestedIterator(object):

    def __init__(self, nestedList):
        self.nestedList = nestedList
        return NestedIterator(nestedList).next(self.nestedList)

    def f(self, n):
        self.n = n
        cnt = 1
        while n is not int:
            i = 0
            while i != len(n):
                if type(n[i]) is not int:
                    n = n[i]
                    cnt += 1
                else:
                    return n[i], cnt

    def next(self, nestedList):
        self.nestedList = nestedList
        i = 0
        if NestedIterator().hasNext(nestedList):
            if type(nestedList[i]) is int:
                res.append(nestedList[i])
                nestedList = nestedList[i + 1:]
            else:
                n, cnt = NestedIterator().f(nestedList[i])
                res.append(n)
                n = [0] * cnt

                del nestedList[i][n[0]]

                if nestedList[i] == []:
                    del nestedList[i]

    def hasNext(self, nestedList):
        return nestedList != []

res = NestedIterator([[1,1],2,[1,1]])