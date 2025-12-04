class BSTNode:
    def height(self):
        if self.val is None:
            return 0
        leftm = self.left.height() if self.left else 0
        rightm = self.right.height() if self.right else 0
        return 1 + max(leftm, rightm)

        # leftm = 0
        # rightm = 0
        # if self.left is not None:
        #     leftm = self.left.height()
        # if self.right is not None:
        #     rightm = self.right.height()
        # return 1 + max(leftm, rightm)

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
