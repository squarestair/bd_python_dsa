class BSTNode:
    def inorder(self, visited):
        print("---START FN----", visited)
        if self.left is not None:
            print("LEFT val: ", self.val, "visited: ", visited)
            self.left.inorder(visited)
        if self.val is not None:
            visited.append(self.val)
            print("MIDDLE val: ", self.val, "visited: ", visited)
        if self.right is not None:
            print("RIGHT val: ", self.val, "visited: ", visited)
            self.right.inorder(visited)
        print("----END FN----", visited)
        return visited

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
