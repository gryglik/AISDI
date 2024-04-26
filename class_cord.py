class cord():
    def __init__(self, x=None, y=None) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'[{self.x} {self.y}]'


class queue_element():
    def __init__(self, dist: int | None, cord: cord) -> None:
        self.dist = dist
        self.cord = cord

    def __lt__(self, q_el: 'queue_element') -> bool:
        return self.dist < q_el.dist


def next_nodes(root, size):
    childs = []
    if root.x > 0:
        childs.append(cord(root.x - 1, root.y))
    if root.y > 0:
        childs.append(cord(root.x, root.y - 1))
    if root.y < size.y - 1:
        childs.append(cord(root.x, root.y + 1))
    if root.x < size.x - 1:
        childs.append(cord(root.x + 1, root.y))
    return childs
