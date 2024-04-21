class AVLNode():
    def __init__(self, key: int | None = None) -> None:
        self.left: AVLNode | None = None
        self.right: AVLNode | None = None
        self.key: int | None = key
        self.h: int = 1

    def balance(self) -> int:
        if not self.left and not self.right:
            return 1
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

    def _rRotate(self) -> 'AVLNode':
        new_root = self.left

        temp = new_root.right
        new_root.right = self
        self.left = temp

        self.h = 1 + self.max_h()
        new_root.h = 1 + new_root.max_h()

        return new_root

    def _lRotate(self) -> 'AVLNode':
        new_root = self.right

        temp = new_root.left
        new_root.left = self
        self.right = temp

        self.h = 1 + self.max_h()
        new_root.h = 1 + new_root.max_h()

        return new_root

    def add(self, key: int) -> 'AVLNode':
        if key > self.key:
            self.right = self.right.add(key) if self.right else AVLNode(key)
        else:
            self.left = self.left.add(key) if self.left else AVLNode(key)

        self.h = 1 + self.max_h()
        balance = self.balance()

        if balance == 2:       # Wychylone w lewo
            if self.left.balance() == 1:       # LL
                return self._rRotate()
            elif self.left.balance() == -1:    # LR
                self.left = self.left._lRotate()
                return self._rRotate()

        elif balance == -2:       # Wychylone w prawo
            if self.right.balance() == -1:      # RR
                return self._lRotate()
            elif self.right.balance() == 1:     # RL
                self.right = self.right._rRotate()
                return self._lRotate()

        return self

    def add_list(self, keys: list[int]) -> 'AVLNode':
        if not self.key:
            self.key = keys[0]
        for key in keys[1:]:
            self = self.add(key)
        return self

    def search(self, key: int) -> None:
        if key == self.key:
            return self
        if key < self.key:
            return self.left.search(key) if self.left else None
        else:
            return self.right.search(key) if self.right else None

    def print(self) -> None:
        queue = [self]
        for node in queue:
            queue.append(node.left if node else None)
            queue.append(node.right if node else None)
            if len(queue) == pow(2, self.h) - 1:
                break

        for level in range(0, self.h):
            spacing = pow(2, self.h - level + 1)
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
