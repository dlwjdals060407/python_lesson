class Boss:
    def __init__(self, x, y, rad, attr=0) -> None:
        self.x=x
        self.y=y
        self.rad=rad
        self.speed = 5
        self.attr = attr