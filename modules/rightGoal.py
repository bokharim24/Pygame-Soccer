import pygame

from .mobile import Mobile
from .animated import Animated
from .drawable import Drawable
from .vector2D import Vector2
import os


class RightGoal(Drawable):
    def __init__(self, position):
        super().__init__("rightGoal.png", position)
