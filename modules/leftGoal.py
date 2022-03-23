import pygame

from .mobile import Mobile
from .animated import Animated
from .drawable import Drawable
from .vector2D import Vector2
import os


class LeftGoal(Drawable):
    def __init__(self, position):
        super().__init__("leftGoal.png", position)
