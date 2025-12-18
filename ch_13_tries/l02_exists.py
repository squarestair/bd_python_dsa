class Trie:
    def exists(self, word):
        cur = self.root
        for letter in word:
            # print(f"Letter = {letter} , curr: {cur}")
            if letter not in cur:
                return False
            cur = cur[letter]
        # print(f"Letter = {letter} , curr: {cur}")
        return self.end_symbol in cur

    # don't touch below this line

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
