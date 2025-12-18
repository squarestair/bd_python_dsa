class Trie:
    def add(self, word):
        cl = self.root
        for i, c in enumerate(word):
            if c not in cl:
                cl[c] = {}
            cl = cl[c]
            if i == len(word) - 1:
                # print("last char:", c)
                cl[self.end_symbol] = True
        # print(f"CL = {cl}")
        # print("end")

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
