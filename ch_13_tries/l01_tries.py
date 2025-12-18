class Trie:
    def add(self, word):
        cl = self.root
        for c in word:
            if c not in cl:
                cl[c] = {}
            cl = cl[c]
        cl[self.end_symbol] = True

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
