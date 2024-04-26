import math


class Heap():
    def __init__(self, a: int = 2, T: list[int | None] = []) -> None:
        """
        Creates an instance of the heap and make heap from given list

        Args:
            a (int, optional): a-ary heap. Defaults to 2.
            T (list[int  |  None], optional): List of keys to create heap.
                Defaults to []. Can be either with T[0] == int or T[0] == None.
        """
        self._a: int = a
        if T[0]:
            self._T: list[int | None] = [None] + T[:]
        else:
            self._T: list[int | None] = T[:]
        self._make_heap()

    def list(self) -> list[int | None]:
        """
        Returns list of elements in heap with None

        Returns:
            list[int | None]: List of elements in heap.
        """
        return self._T[:]

    def len(self) -> int:
        """
        Returns length of heap without None

        Returns:
            int: Returns length of heap
        """
        return len(self._T) - 1

    def right(self, n: int) -> int | None:
        """
        Returns index of last child of given parent.

        Last child of given parent is located at index:
        n * a + 1 (+ 1 move to right).

        Args:
            n (int): parent index

        Returns:
            int | None: last child index or None if no child
        """
        right = n * self._a + 1 if n * self._a + 1 <= self.len() else self.len()
        return right if right <= self.len() else None

    def left(self, n: int) -> int | None:
        """
        Returns index of first child of given parent

        First child of given parent is located at index
        right() - (a - 1) = n * a + 1 - (a - 1) = (n - 1) * a + 2

        Args:
            n (int): parent index

        Returns:
            int | None: first child index or None if no child
        """
        return (n - 1) * self._a + 2 if (n - 1) * self._a + 2 <= self.len() else None

    def parent(self, n: int) -> int | None:
        """
        Returns index of parent of given child or None if no parent.

        children indexes are:
            [(x - 1) * a + 2, x * a + 1]
        to get parent index (x) we have to:
            1) shift children indexes by (a - 2)
                then chlildren indexes are [x * a, (x + 1) * a - 1]
            2) divide them by degree of heap (a)

        Args:
            n (int): index of child

        Returns:
            int | None: index of parent
        """
        if n == 1:
            return None
        return (n + self._a - 2) // self._a

    def _swap(self, i: int, j: int) -> None:
        """
        Swaps two keys in heap.

        Args:
            i (int): first index
            j (int): second index
        """
        temp = self._T[i]
        self._T[i] = self._T[j]
        self._T[j] = temp

    def _heapify(self, n: int) -> None:
        """
        Creates a heap for given apex(n) provided that
        children of n are also heaps.

        Args:
            n (int): index of apex
        """
        if self.left(n):
            i_max = self.left(n)
            for i in range(self.left(n) + 1, self.right(n) + 1):
                if self._T[i] > self._T[i_max]:
                    i_max = i
            if self._T[i_max] > self._T[n]:
                self._swap(i_max, n)
                self._heapify(i_max)

    def _make_heap(self) -> None:
        """
        Creates heap by doing heapify starting from last node (not leaf)

        After every 7th element new node is created starting from 2nd, that's
        why  (length - 2) // a increases when new node is created, we need to
        add 1 becouse heap always has at least 1 node.
        """
        for i in range(1 + (self.len() - 2) // self._a, 0, -1):
            self._heapify(i)

    def add(self, new_item: int) -> None:
        """
        Adds new item to heap and fix it.

        Args:
            new_item (int): new item key.
        """
        self._T.append(new_item)
        i_item = self.len()
        i_parent = self.parent(i_item)
        while i_parent and self._T[i_item] > self._T[i_parent]:
            self._swap(i_item, i_parent)
            i_item = i_parent
            i_parent = self.parent(i_item)

    def remove_root(self) -> None:
        """
        To remove the root:
        * swap root with the last_element
        * delete root (right now last element of a list)
        * heapify make right heap again from root
        """
        self._swap(1, self.len())
        self._T.pop()
        self._heapify(1)

    def level(self) -> int:
        """
        Compute the how many levels heap have from this formula
        Sum of geometric series
        Sn = (1 - a^n)/(1-a) ->
        Sn(1-a) = (1 - a^n) ->
        a^n = Sn(a-1) + 1
        n = loga(Sn(a-1)+1)
        Sn - amount of elements for full heap
        a - a-ary heap how many childs node have
        n - how many levels tree have
        We have a and Sn(self._len) so we compute ~n
        """
        formula = (self._a-1) * self.len() + 1

        # Obliczenie logarytmu o podstawie x
        level = math.log(formula) / math.log(self._a)
        return math.ceil(level)

    def print(self) -> None:
        spaces = self._a ** (self.level() - 1)
        count = 1
        first_in_row = 1
        while (first_in_row <= self.len()):
            end_in_row = min(first_in_row+count, self.len()+1)
            print(' '*int(spaces) + str(self._T[first_in_row:end_in_row]))
            first_in_row += count
            count *= self._a
            spaces -= math.ceil(count)
