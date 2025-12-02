from l08_node import Node


class LLQueue:
    def remove_from_head(self):
        if not self.head:
            return None
        if self.head.next is None:
            self.tail = None
        temp = self.head
        self.head = self.head.next
        temp.set_next(None)
        return temp

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)
