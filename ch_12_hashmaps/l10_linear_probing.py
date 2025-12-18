class HashMap:
    def insert(self, key, value):
        ind = self.key_to_index(key)
        original_index = ind
        first_iteration = True
        while self.hashmap[ind] is not None and self.hashmap[ind][0] != key:
            if not first_iteration and ind == original_index:
                raise Exception("hashmap is full")
            ind = (ind + 1) % len(self.hashmap)
            first_iteration = False
        self.hashmap[ind] = (key, value)

    def get(self, key):
        ind = self.key_to_index(key)
        original_index = ind
        first_iteration = True
        while self.hashmap[ind] is not None:
            if self.hashmap[ind][0] == key:
                return self.hashmap[ind][1]
            elif not first_iteration and ind == original_index:
                raise Exception("sorry, key not found")
            ind = (ind + 1) % len(self.hashmap)
            first_iteration = False

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
