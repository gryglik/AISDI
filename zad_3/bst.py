class Node():
    def __init__(self, key: int) -> None:
        self.left = None
        self.right = None
        self.key = key


class BST():
    def __init__(self, keys: list[int] = []) -> None:
        self.nodes: list[Node | None] = []
        self.root = None
        for key in keys:
            self.add(self.root, key)

    def add_key(self, key):
        self.add(self.root, key)

    def add(self, node: Node, key) -> Node:
        if self.root is None:
            self.root = Node(key)
        if node is None:
            return Node(key)
        else:
            if key == node.key:
                return node
            elif node.key < key:
                node.right = self.add(node.right, key)
            else:
                node.left = self.add(node.left, key)
        return node

    def search(self, node, key) -> int | None:
        if node is None or node.key == key:
            return node

        if node.key < key:
            return self.search(node.right, key)

        return self.search(node.left, key)

    def remove(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self.remove(node.left, key)
        elif key > node.key:
            node.right = self.remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.key = self.smaller_child(node.right)

            node.right = self.remove(node.right, node.key)

        return node

    def smaller_child(self, node):
        child = node.key
        while node.left:
            child = node.left.key
            node = node.left
        return child

    def size(self) -> int:
        return len(self.nodes)

    def height(self, node: Node | None) -> int:
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def print(self) -> None:
        queue = [self.root]
        for node in queue:
            queue.append(node.left if node else None)
            queue.append(node.right if node else None)
            if len(queue) == pow(2, self.height(self.root)) - 1:
                break

        for level in range(0, self.height(self.root)):
            spacing = pow(2, self.height(self.root) - level + 1)
            s = ' ' * spacing

            struct = ' ' * (spacing + spacing // 2)
            k = 0
            for element in range(0, pow(2, level)):
                node = queue.pop(0)

                if k % 2 == 0:
                    if node:
                        struct += '/'
                    else:
                        struct += " "
                    struct += ' ' * (spacing - 1)
                    s += " " if not node else str(node.key)
                    s += " " * (2 * spacing - 1)
                else:
                    if node:
                        struct += chr(92)
                    else:
                        struct += " "
                    struct += ' ' * (3 * spacing - 1)
                    s += " " if not node else str(node.key)
                    s += " " * (2 * spacing - 1)
                k += 1
            if level > 0:
                print(struct)
            print(s)
