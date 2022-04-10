from .drawable import Drawable

#A class for the right goal
class RightGoal(Drawable):
    def __init__(self, position):
        super().__init__("rightGoal.png", position)
