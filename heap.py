class Heap():
    def __init__(self, a: int = 2, T: list[int | None] = []) -> None:
        self._a: int = a
        if T[0]:
            self._T: list[int | None] = [None] + T[:]
        else:
            self._T: list[int | None] = T[:]
        self._make_heap()

    def list(self) -> list[int | None]:
        return self._T[:]

    def len(self) -> int:
        return len(self._T) - 1 # bez None

    def right(self, n: int) -> int | None:
        # ostatnie dziecko danego rodzica znajduje się pod indeksem
        # n * a + 1 - przesunięcie w prawo
        right = n * self._a + 1 if n * self._a + 1 <= self.len() else self.len()
        return right if right <= self.len() else None

    def left(self, n: int) -> int | None:
        # pierwsze dziecko danego rodzica znajduje się pod indeksem
        # right() - (a - 1) = n * a + 1 - (a - 1) = (n - 1) * a + 2
        return (n - 1) * self._a + 2 if (n - 1) * self._a + 2 <= self.len() else None

    def parent(self, n: int) -> int | None:
        if n == 1:
            return None
        # indeksy dzieci [(x - 1) * a + 2, x * a + 1], więc aby uzyskać
        # indeks rodzica x należy przesunąć indeksy dzieci o +(a - 2)
        # wtedy przesunięte indeksy dzieci [x * a, (x + 1) * a - 1]
        # dzielone przez stopień kopca (a) daje indeks rodzica (x)
        return (n + self._a - 2) // self._a

    def _swap(self, i: int, j: int) -> None:
        temp = self._T[i]
        self._T[i] = self._T[j]
        self._T[j] = temp

    def _heapify(self, n: int) -> None:
        if self.left(n):
            i_max = self.left(n)
            for i in range(self.left(n) + 1, self.right(n) + 1):
                if self._T[i] > self._T[i_max]:
                    i_max = i
            if self._T[i_max] > self._T[n]:
                self._swap(i_max, n)
                self._heapify(i_max)

    def _make_heap(self) -> None:
        for i in range(1 + (self.len() - 2) // self._a, 0, -1):
            self._heapify(i)

    def add(self, new_item: int) -> None:
        self._T.append(new_item)
        i_item = self.len()
        i_parent = self.parent(i_item)
        while i_parent and self._T[i_item] > self._T[i_parent]:
            self._swap(i_item, i_parent)
            i_item = i_parent
            i_parent = self.parent(i_item)
