from l05_node import Node


class LinkedList:
    def add_to_tail(self, node):
        if not self.head:
            self.head = node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = node
        # Alternate solution
        # for current_node in self:
        #     last_node = current_node
        # last_node.set_next(node)

    # don't touch below this line

    def __init__(self):
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
        return " -> ".join(nodes)
