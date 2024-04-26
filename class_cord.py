class cord():
    def __init__(self, x=None, y=None) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'[{self.x} {self.y}]'
