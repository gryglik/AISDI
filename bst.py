class Node():
    def __init__(self, parent: int, left: int | None,
                 right: int | None, key: int) -> None:
        self.parent = parent
        self.left = left
        self.right = right
        self.key = key


class BST():
    def __init__(self, keys: list[int] = []) -> None:
        self.nodes: list[Node | None] = []
        for key in keys:
            self.add(key)

    def add(self, key):
        if self.size() == 0:
            root = Node(0, None, None, key)
            self.nodes.append(root)
        else:
            curr_node = self.nodes[0]
            new = Node(0, None, None, key)
            while (curr_node.parent is not None
                   and curr_node.parent < self.size()):
                if new.key < curr_node.key:
                    # Our key is smaller so we go to the left child
                    if curr_node.left:
                        # Left exists = we go to left and checks his children
                        new.parent = curr_node.left
                        curr_node = self.nodes[curr_node.left]
                    else:
                        # Left doesnt exist - we create left from new key
                        curr_node.left = self.size()
                        self.nodes.append(new)
                        break
                else:
                    # Our key is bigger so we go to the right child
                    if curr_node.right:
                        # if right exist we go to right in recursion
                        new.parent = curr_node.right
                        curr_node = self.nodes[curr_node.right]
                    else:
                        # if right doesnt exist we create right with new node
                        curr_node.right = self.size()
                        self.nodes.append(new)
                        break

    def search(self, key) -> int | None:
        if self.size() == 0:
            return None
        else:
            curr_node = self.nodes[0]
            if curr_node.key == key:
                return 0

            while (curr_node.parent is not None
                   and curr_node.parent < self.size()):
                # Go left
                if key < curr_node.key:
                    print(f'go right {key}')
                    # Checks if left exist
                    if curr_node.left is None:
                        return None
                    if self.nodes[curr_node.left].key == key:
                        return curr_node.left
                    else:
                        curr_node = self.nodes[curr_node.left]
                # Go right
                else:
                    print(f'go left {key}')
                    # Checks if right exist
                    if curr_node.right is None:
                        return None
                    if self.nodes[curr_node.right].key == key:
                        return curr_node.right
                    else:
                        curr_node = self.nodes[curr_node.right]
        return None

    def size(self) -> int:
        return len(self.nodes)

    def key_list(self) -> list[int]:
        return [node.key for node in self.nodes]
