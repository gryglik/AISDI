class AVLNode():
    def __init__(self, parent: 'AVLNode', key: int) -> None:
        self.parent: AVLNode = parent
        self.left: AVLNode | None = None
        self.right: AVLNode | None = None
        self.key: int = key
        self.h: int = 1

    def balance(self) -> int:
        if not self.left:
            return -self.right.h
        if not self.right:
            return self.left.h
        return self.left.h - self.right.h

    def max_h(self) -> int:
        if not self.left and not self.right:
            return 0
        if not self.left:
            return self.right.h
        if not self.right:
            return self.left.h
        return max(self.left.h, self.right.h)


class AVL():
    def __init__(self, keys: list[int]) -> None:
        self._root = AVLNode(None, keys[0])
        for key in keys[1:]:
            self.add(key)

    def _binaryAdd(self, new_node: AVLNode, root: AVLNode) -> AVLNode:
        key = new_node.key
        if key > root.key:
            if not root.right:
                new_node.parent = root
                root.right = new_node
            else:
                self._binaryAdd(new_node, root.right)
        else:
            if not root.left:
                new_node.parent = root
                root.left = new_node
            else:
                self._binaryAdd(new_node, root.left)

    def _rRotate(self, node: AVLNode) -> None:
        new_root = node.left

        temp = new_root.right
        new_root.right = node
        new_root.parent = node.parent
        if node.parent:
            if node.parent.left == node:
                node.parent.left = new_root
            else:
                node.parent.right = new_root
        node.parent = new_root
        node.left = temp
        if node.left:
            node.left.parent = node

        if not new_root.parent:
            self._root = new_root

        node.h = 1 + node.max_h()
        new_root.h = 1 + new_root.max_h()

        return new_root

    def _lRotate(self, node: AVLNode) -> None:
        new_root = node.right

        temp = new_root.left
        new_root.left = node
        new_root.parent = node.parent
        if node.parent:
            if node.parent.left == node:
                node.parent.left = new_root
            else:
                node.parent.right = new_root
        node.parent = new_root
        node.right = temp
        if node.right:
            node.right.parent = node

        if not new_root.parent:
            self._root = new_root

        node.h = 1 + node.max_h()
        new_root.h = 1 + new_root.max_h()

        return new_root

    def _balance(self, node: AVLNode) -> None:
        if not node:
            return

        if not node.left:
            node.h = 1 + node.right.h
        elif not node.right:
            node.h = 1 + node.left.h
        else:
            node.h = 1 + max(node.left.h, node.right.h)

        if node.balance() == 2:       # Wychylone w lewo
            if node.left.balance() == 1:       # LL
                node = self._rRotate(node)
            elif node.left.balance() == -1:    # LR
                self._lRotate(node.left)
                node = self._rRotate(node)

        elif node.balance() == -2:       # Wychylone w prawo
            if node.right.balance() == -1:      # RR
                node = self._lRotate(node)
            elif node.right.balance() == 1:     # RL
                self._rRotate(node.right)
                node = self._lRotate(node)

        self._balance(node.parent)

    def add(self, key: int) -> None:
        new_node = AVLNode(None, key)
        self._binaryAdd(new_node, self._root)
        self._balance(new_node.parent)

    def _search(self, key: int, node: AVLNode = None) -> AVLNode | None:
        if not node:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self._search(key, node.left)
        else:
            return self._search(key, node.right)

    def search(self, key: int) -> AVLNode:
        return self._search(key, self._root)
