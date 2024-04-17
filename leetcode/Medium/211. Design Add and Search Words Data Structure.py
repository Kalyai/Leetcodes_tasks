class wordNode:
    def __init__(self):
        self.node = {}
        self.endWord = False


class WordDictionary(object):
    def __init__(self):
        self.root = wordNode()

    def addWord(self, word):
        tree = self.root

        for string in word:
            if string not in tree.node:
                tree.node[string] = wordNode()
            tree = tree.node[string]
        tree.endWord = True

    def search(self, word):
        tree = self.root

        def dfs(tree, word):
            for i in range(len(word)):
                if word[i] == '.':
                    for child in tree.node.values():
                        if dfs(child, word[i + 1:]):
                            return True
                    return False

                else:
                    if word[i] not in tree.node:
                        return False
                    tree = tree.node[word[i]]

            if tree.endWord:
                return True
            return False

        return dfs(tree, word)
