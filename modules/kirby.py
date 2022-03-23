from modules.animated import Animated


class Kirby(Animated):
    def __init__(self, position):
        super().__init__("kirby.png", position)

        self._nFrames = 4
        self._row = 1
