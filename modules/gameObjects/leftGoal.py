
from .drawable import Drawable

#A class for the left goal
class LeftGoal(Drawable):
    def __init__(self, position):
        super().__init__("leftGoal.png", position)
    
   