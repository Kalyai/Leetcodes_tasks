class TrieNode:
    def __init__(self):
        self.node = {}
        self.endWord = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        tree = self.root

        for string in word:
            if string not in tree.node:
                tree.node[string] = TrieNode()
            tree = tree.node[string]
        tree.endWord = True


    def search(self, word):
        tree = self.root

        for string in word:
            if string not in tree.node:
                return False
            tree = tree.node[string]

        if tree.endWord:
            return True
        return False

    def startsWith(self, prefix):
        tree = self.root

        for string in prefix:
            if string not in tree.node:
                return False
            tree = tree.node[string]
        return True
