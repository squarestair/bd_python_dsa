class BSTNode:
    def exists(self, val):
        if self.val == val:
            return True
        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)

        # Initial solution:
        # if self.val == val:
        #     return True
        # if self.left is not None:
        #     if self.left.exists(val):
        #         return True
        # if self.right is not None:
        #     if self.right.exists(val):
        #         return True
        # return False

        # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
